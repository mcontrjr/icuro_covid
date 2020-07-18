import cv2


## get_size: get size of the image given the path
def get_size(img_path):
	im = cv2.imread(img_path)
	width = im.shape[1]
	height = im.shape[0]
	return width, height

## convert_label: convert the OID labe (right, top, left, bottom)
## to YOLO label (xcenter, ycenter, width, height).
def convert_label(width, height, label):
	label = label.split("\n")[0]
	label = label.split(" ")
	length = len(label)-1
	left, top, right, bottom = label[length-3:]
	box_w = (float(right)-float(left))
	box_h = (float(bottom)-float(top))
	w = (box_w)/width
	h = (box_h)/height
	x = (float(left) + box_w/2)/width
	y = (float(top) + box_h/2)/height
	return x,y,w,h

## write_label: write new YOLO label to to imgID.txt
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