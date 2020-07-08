## convert_to_yolo.py: convert OID labels (right, top, left, bottom) 
## to YOLO label (xcenter, ycenter, width, height) and write them to a .txt
## file to match the corresponding image ID. 


import glob
# print(glob.glob("/home/adam/*.txt"))
from os import listdir, getcwd, walk
from os.path import isfile, join
import cv2
from shutil import copy

## descriptiom: get size of the image given the path
def get_size(img_path):
	im = cv2.imread(img_path)
	width = im.shape[1]
	height = im.shape[0]
	return width, height

## description: convert the OID labe (right, top, left, bottom) 
## to YOLO label (xcenter, ycenter, width, height).
def convert_label(width, height, label):
	label = label.split("\n")[0]
	label = label.split(" ")
	length = len(label)-1
	left, top, right, bottom = label[length-3:]
	w = (float(right)-float(left))/width
	h = (float(bottom) - float(top))/height
	x = (float(left) + w/2)/width
	y = (float(top) + h/2)/height
	return x,y,w,h

## description: write new YOLO label to to imgID.txt
def write_label(class_path, imgID, x,y,w,h, classID, f):
	label = str(classID) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n"
	f.write(label)


## create_dictionary: make dictionary from obj.names
def create_dictionary(names_file):
	f_classes = open(names_file, "r")
	ID = 0
	class_dict = {}
	for classes in f_classes:
		classes = classes.split("\n")[0]
		class_dict.update({classes : ID})
		ID += 1
	f_classes.close()
	return class_dict

# -----------------------------------------

mypath = getcwd()

names_file = '/Users/mcontr/repos/icuro_local/data_for_colab/obj.names'
class_dict = create_dictionary(names_file)
# print(class_dict)
for classes in class_dict:
	class_path = mypath + '/' + classes
	img_paths = listdir(class_path)
	destination = "data"
# 	# Convert all images in the class folders
	for img in img_paths:
		try: 
			imgID = img.split('.')[0]
			img_path = class_path + '/' + img
			if not isfile(destination + '/' + img):
				copy(img_path, destination)
				path = destination + '/' + imgID + '.txt'
				f = open(path, "w")
			else:
				print(img_path)
				path = destination + '/' + imgID + '.txt'
				f = open(path, "a")

			label_path = class_path + '/Label/' + imgID + '.txt'
			file = open(label_path, "r")
			for label in file:
				img_w, img_h = get_size(img_path)
				x,y,w,h = convert_label(img_w, img_h, label)
				write_label(class_path, imgID, x,y,w,h, class_dict[classes], f)
				f.close()
		except:
			continue
			