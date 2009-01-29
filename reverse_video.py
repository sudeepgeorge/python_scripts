#Python script to reverse a video. Does not handle the audio!
# Requires Python and FFmpeg to be installed with the associated libraries like libavcodec/libavformat/libavutil/libavdevice

#Tested using the below versions -
#FFmpeg version r11872+debian_3:0.svn20080206-12ubuntu3, Copyright (c) 2000-2008 Fabrice Bellard, et al.
#Python 2.5.2

import os
import sys
import shutil
import subprocess

#Name of the input file to be reversed"
src_file="prada.mov"

#Name of the output file"
dst_file="reverse.mpg"

#The bitrate at which the output file is to be encoded
bit_rate=1411000


#Commands being used
dump_cmd=['ffmpeg','-i',src_file,'-f','image2','tmp1/%05d.png']

movie_cmd=['ffmpeg','-i','tmp2/%05d.png','-b',str(bit_rate),dst_file]


#Function to delete a sub-directory
def rm_sub_dir(dir_name):
  os.chdir(os.getcwd()+"/"+dir_name)
  dir_list = os.listdir(os.getcwd())
  for i in dir_list:
    os.remove(i)
  os.chdir("..")
  os.removedirs(dir_name)


#Delete the temp directories if present
if(os.path.isdir('tmp1')):
    rm_sub_dir('tmp1')

if(os.path.isdir('tmp2')):
    rm_sub_dir('tmp2')

if(os.path.isfile(dst_file)):
  os.remove(dst_file)



os.mkdir('tmp1')
os.mkdir('tmp2')


#Dump the input movie as a set of frames
subprocess.call(dump_cmd)
num_frames =(len(os.listdir(os.getcwd()+'/tmp1')))+1

#Reversing the frames
print "Copying...",
sys.stdout.flush() 
for i in range(1,num_frames):
	src_name = (str(num_frames-i)).zfill(5)+".png"
	dst_name = (str(i)).zfill(5)+".png"
	shutil.copy("./tmp1/"+src_name,"./tmp2/"+dst_name)
print "Done"


#Create movie with the reversed frames
subprocess.call(movie_cmd)

#Delete tmp stuff
rm_sub_dir('tmp1')
rm_sub_dir('tmp2')



