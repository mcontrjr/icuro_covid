## change_path.py: change the path of a file to a new one

train = "train.txt"
test = "test.txt"

current_path = "/Users/mcontr/repos/icuro/train/"
store_path = "/Users/mcontr/repos/icuro/data_for_colab/"

new_dir = "/content/darknet/data_for_colab/data/"


# copy train.txt

train_path = current_path + train
f_train = open(train_path, "r")

train = store_path + train
new_train = open(train, "w")

for file in f_train:
	file = file.split("/")[-1]
	file = new_dir + file 
	print(file)
	new_train.write(file)

new_train.close()

# copy test.txt

test_path = current_path + test
f_test = open(test_path, "r")

test = store_path + test
new_test = open(test, "w")
for file in f_test:
	file = file.split("/")[-1]
	file = new_dir + file 
	new_test.write(file)

new_test.close()

