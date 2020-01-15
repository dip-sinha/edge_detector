This is a computer vision for my another project. This is a part of the program and with a littel modifications I have made this module.
This Python code opens two windows which shows original video feed and another shows video feed after edge detection. 
I am using a function named Generate_filename() to generate file name for a jpg file. This function resides in another python file named File_name_gen.py
The File_name_gen.py helps to find if there is any folder named images, if there is no folder this python script makes a folder named image and generates a file name as 1000001
If there is a folder but no jpg file in the image folder then it also generates file name as 1000001
if there is a folder in the root directory the scripts searchs for jpg file inside the folder and if there is a jpg file it searches for the last saved image
Reads the last saved image using getctime() function
Then program increments the image name by 1.
it saves images by pressing space bar

TO RUN THE PROJECT
just cd in to the main prooject folder
and use this command:

python edge_detect.py
