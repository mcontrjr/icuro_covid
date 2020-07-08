# icuro covid-19 initiative project

This repo is meant for the computer vision portion of the covid-19 initiative project.

## \cfg 
This folder has existing configuration files for existing YOLO architectures. 

## \weights
This folder holds the weights for the DNN after being trained. 

## \data_for_colab 
The data and necessary files needed for training can be found here. To train, zip this folder and drop it in your Google Drive under a specified folder.

## \train
Folders for the datasets for each respective class (i.e. light switches, door handles, etc.). They also include .txt files with the annotations for the images in the following format:
class_ID x_center y_center width height 
All annotations are with respect to the size of the image and are less than one. 

## run_yolo.ipynb 
Script to run the trained YOLO network using default camera. 

## train_dnn.ipynb
To train, paste this script into Google Drive and run it using Google Colaoratory. Connect to a host runtime and run the session on GPU. 



