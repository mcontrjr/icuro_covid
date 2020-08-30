# oid_process.py: process the images that have multiple labels in their respectuve dataset.
from os import listdir, getcwd, mkdir
from os.path import isdir, isfile
from glob import glob
from shutil import copy

import os

from console_progressbar import ProgressBar

from utils.helpers import *

pb = ProgressBar(total=100,prefix='Progress', decimals=3, length=50, fill='•', zfill='-')

def oid_process():
	oid_path = "/home/atlas/repos/OIDv4_ToolKit/OID/Dataset/train"
	names_file = '../data_to_train/obj.names'
	class_dict,master_list = create_dictionary(names_file)
	download_th = 100000
	total = 0
	# Look for duplicates
	for classes in class_dict:
		class_path = os.path.join(oid_path,classes)
		class_list = glob(os.path.join(class_path,"*.jpg"))
		print("{}: {}".format(classes,len(class_list)))
		destination = "/home/atlas/repos/darknet/data_to_train/data"
		# Convert all images in the class folders
		if not isdir(destination):
			# Make directory if it doesn't exist
			print("Making /data folder in darknet. . .")
			mkdir(destination)
		exist = []
		queue = []
		remaining_imgs = []
		downloads = 0
		for img in class_list:
			img = img.split("/")[-1]
			if isfile(os.path.join(destination,img)):
				exist.append(img)
			elif check_classes(img,classes,class_dict,master_list):
				queue.append(img)
			else:
				remaining_imgs.append(img)
		if len(exist) < 150:
			queue.extend(remaining_imgs)
		print("{} images exist, {} images in queue...".format(len(exist), len(queue)))
		
		for img in exist:
			imgID = img.split('.')[0]
			img_path = class_path + '/' + img 
			path = destination + '/' + imgID + '.txt'
			f = open(path, "a")
			downloads += 1
			label_path = class_path + '/Label/' + imgID + '.txt'
			file = open(label_path, "r")
			for label in file:
				img_w, img_h = get_size(img_path)
				x,y,w,h = convert_label(img_w, img_h, label)
				classID = class_dict[classes]
				label = str(classID) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n"
				f.write(label)
			f.close()
		remaining = download_th - downloads
		print("Added {} annotations".format(downloads))
		downloads = 0
		for img in queue:
			if downloads == remaining:
				break
			imgID = img.split('.')[0]
			img_path = class_path + '/' + img 
			copy(img_path, destination)
			downloads += 1
			path = destination + '/' + imgID + '.txt'
			f = open(path, "w")
			label_path = class_path + '/Label/' + imgID + '.txt'
			file = open(label_path, "r")
			for label in file:
				img_w, img_h = get_size(img_path)
				x,y,w,h = convert_label(img_w, img_h, label)
				classID = class_dict[classes]
				label = str(classID) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n"
				f.write(label)
			f.close()
			pcnt = downloads/download_th*100
			pb.print_progress_bar(pcnt)
		total += downloads
		print("Downloaded {} images\n\t -----------".format(downloads))
	print("Total images: {}".format(total))
