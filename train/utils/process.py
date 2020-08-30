import glob, os


<<<<<<< HEAD
def process():
    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

#    print("Current Directory: " + current_dir)
=======
def process(train_dir):
    counter = 0
    files = 0
    print("Data Directory: " + train_dir)
>>>>>>> 8d25be06... data folder is now in darknet. this repo has preprocess that looks through the names and generates AB

    ##      Directory to write to    ##
    write_dir ="/Users/mcontr/repos/icuro_covid/data_to_train" # Local Computer

    # Percentage of images to be used for the test set
    percentage_test = 10;

    # Create and/or truncate train.txt and test.txt into
    file_train = open((write_dir + '/train.txt'), 'w')
    file_test = open((write_dir + 'test.txt'), 'w')

    # Populate train.txt and test.txt
    counter = 1
    index_test = round(100 / percentage_test)
<<<<<<< HEAD
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        ## write to train and test .txt files with correct training directory
        if counter == index_test:
            counter = 1
            file_test.write(train_dir + "/" + title + '.jpg' + "\n")
        else:
            file_train.write(train_dir + "/" + title + '.jpg' + "\n")
            # counter = counter + 1 # uncomment to add test.txt
=======
    for pathAndFilename in glob.iglob(os.path.join(train_dir, "*.jpg")):
        # print(pathAndFilename)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if ext == 'jpg':
                print(title)
        ## write to train and test .txt files with correct training directory
        if files%percentage_test == 0:
            files += 1
            file_test.write(train_dir + title + '.jpg' + "\n")
            
        else:
            files += 1

            file_train.write(train_dir + title + '.jpg' + "\n")

    for pathAndFilename in glob.iglob(os.path.join(train_dir, "*.JPG")):
        # print(pathAndFilename)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        ## write to train and test .txt files with correct training directory
        if files%percentage_test == 0:
            files += 1
            file_test.write(train_dir + title + '.JPG' + "\n")
            
        else:
            files += 1
            file_train.write(train_dir + title + '.JPG' + "\n")
        
    file_train.close()
    file_test.close()
    print("Total image paths: %d" % files)

	
>>>>>>> 8d25be06... data folder is now in darknet. this repo has preprocess that looks through the names and generates AB
