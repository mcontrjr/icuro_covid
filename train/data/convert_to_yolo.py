## convert_to_yolo.py: convert OID labels (right, top, left, bottom) 
## to YOLO label (xcenter, ycenter, width, height) and write them to a .txt
## file to match the corresponding image ID. 


import glob,os
# print(glob.glob("/home/adam/*.txt"))
from os import listdir, getcwd, mkdir
from os.path import isfile, join, isdir
import cv2
from shutil import copy

from utils.helpers import *
from utils.process import *
# from utils

# -----------------------------------------

def main():
	mypath = getcwd()
	duplicates = 0
	names_file = '/Users/mcontr/repos/icuro_covid/data_to_train/obj.names'
	class_dict = create_dictionary(names_file)
	# print(class_dict)
	for classes in class_dict:
		class_path = mypath + '/' + classes
		img_paths = listdir(class_path)
		print(classes + ": " + str(len(img_paths)))
		destination = "data"
		# Convert all images in the class folders
		if not isdir("data"):
			make_data = os.path.join(getcwd(), destination)
			mkdir(make_data)
		for img in img_paths:
			try:
				imgID = img.split('.')[0]
				img_path = class_path + '/' + img

				if not isfile(destination + '/' + img):
					copy(img_path, destination)
					path = destination + '/' + imgID + '.txt'
					f = open(path, "w")
				else:
					# print(img_path) # print duplicates
					path = destination + '/' + imgID + '.txt'
					f = open(path, "a")
					duplicates += 1

				label_path = class_path + '/Label/' + imgID + '.txt'
				file = open(label_path, "r")
				for label in file:
					img_w, img_h = get_size(img_path)
					x,y,w,h = convert_label(img_w, img_h, label)
					write_label(class_path, imgID, x,y,w,h, class_dict[classes], f)
					f.close()
			except:	continue
				# print("Could not find %s" %img)	
	print("There were %d duplicates" % duplicates)
	process()


if __name__ == '__main__':
	main()
			
