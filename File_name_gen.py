import os
import glob
import imghdr
import ntpath
cwd = os.getcwd()
image_dir = cwd+"/image"
file = image_dir+"/*.jpg"

def last_saved():
    # find last saved image in a directory
    list_of_files = glob.glob(image_dir+'/*.jpg')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    head,tail = os.path.split(latest_file)
    file_name = os.path.splitext(tail)[0]
    return file_name
    # returns file name without extension
def dir_exists():
    isdir= os.path.isdir("./image")
    return isdir
    # returns true or false
def file_exists():
    for root, dirs, files in os.walk("./image", topdown=False):
        for file in files:
            if file.endswith(".jpg"):
                res = "yes"
            else:
                res = "no"
    return res
def Generate_filename():
#get jpg file details from last saved image

    #check the current directory if there is any folder named image

    if dir_exists() == True:
        # find if there is any jpg file. if there is a jpg file then call function last_saved()
        if file_exists() == "yes":
            last_filename = last_saved()
            last_file = int(last_filename)
            #print("last_filename :", last_file)
            last_file += 1 # increment number by one
            new_filename = last_file

        else:
            new_filename = '1000001'

            # and do the process of previous if loop again
            # if there is file continue the filename with 1 increment in name

    else:
        #creat dir if image folder does not exists!
        # if there is no jpg file start the name from 00000001.jpg
        os.mkdir(image_dir)
        new_filename = '1000001'
    return new_filename


print("file will be saved as:", Generate_filename(), ".jpg")
