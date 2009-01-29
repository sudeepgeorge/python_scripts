#Python script to create a timelapsed video. Does not handle the audio!
# Requires Python and FFmpeg to be installed with the associated libraries like libavcodec/libavformat/libavutil/libavdevice

#Tested using the below versions -
#FFmpeg version r11872+debian_3:0.svn20080206-12ubuntu3, Copyright (c) 2000-2008 Fabrice Bellard, et al.
#Python 2.5.2

import os
import sys
import subprocess

#Name of the input file."
src_file="reverse.mpg"

#Name of the output file"
dst_file="timelapse.mpg"

#The timelapse frame rate for the input video
framerate=1

#The bitrate at which the output file is to be encoded
bit_rate=1411000


#Commands being used
dump_cmd=['ffmpeg','-i',src_file,'-r',str(framerate),'-f','image2','tmp/%05d.png']

movie_cmd=['ffmpeg','-i','tmp/%05d.png','-b',str(bit_rate),dst_file]

#Function to delete a sub-directory
def rm_sub_dir(dir_name):
  os.chdir(os.getcwd()+"/"+dir_name)
  dir_list = os.listdir(os.getcwd())
  for i in dir_list:
    os.remove(i)
  os.chdir("..")
  os.removedirs(dir_name)

#Delete the temp directories if present
if(os.path.isdir('tmp')):
  rm_sub_dir('tmp')

if(os.path.isfile(dst_file)):
  os.remove(dst_file)

os.mkdir('tmp')

#Dump the input movie as a set of frames at a reduced frame rate
subprocess.call(dump_cmd)

#Create the timelapsed movie
subprocess.call(movie_cmd)

#Delete tmp stuff
rm_sub_dir('tmp')