'''
preprocess.py: preprocess OID dataset and generate the anchor boxes. Generate train.txt
and test.txt to /data folder with data paths.
'''
from utils.add_icuro import *
from utils.oid_process import *
from utils.anchors import *
from utils.process import *
from utils.augment import *
def main():
	# # Process OID dataset
	# oid_process() # uncomment when we add new data

	# # Augment the ICURO data
	# augment_icuro()
	
	# # Add custom ICURO dataset
	# add_icuro()

	# Generate train and test .txt files to calculate anchor boxes with k-clustering
	print("Processing images ...")
	data_dir = "/home/atlas/repos/darknet/data_to_train/data/"
	process(data_dir)

	# run() generates anchor6.txt and anchor9.txt for tinyYOLO and YOLO models
	print("Generating anchor boxes...")
	run()


if __name__ == '__main__':
	main()
