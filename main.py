#!/usr/bin/env python3

# -*- coding: utf-8 -*-

## this project uses GNU GPL v3 license

## coded by ddjanic@yandex.ru (@ddjanic) 01-10-2023

import os, shutil, subprocess

# def remove normal folder 
def rrem_folder(path):
    shutil.rmtree(path, ignore_errors=True, onerror=None, dir_fd=None)
# def hidden && RO folder (unmask it)
def on_ro_error(func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)
    
#############################
#
# set your ragnarok game folder with \\
ROtarget = r"R:\\_games\\rgROprime"
# set your user folder
USRtarget = r"C:\\Users\\ddjanic"

# remove read-only flag for whole game folder
if os.path.exists(ROtarget) :
    subprocess.check_call(('attrib -R ' + ROtarget + '\\* /S').split())

# folders:
# tmp    
rrem_folder("C:\\tmp")
rrem_folder("C:\\Temp")
# win temp
rrem_folder("C:\\Windows\\Temp")
# usr profile temp
rrem_folder(USRtarget + "\\AppData\\Local\\Temp")
# usr profile
rrem_folder(USRtarget + "\\AppData\\Local\\Innova")
# usr profile
rrem_folder(USRtarget + "\\AppData\\Local\\Innova_Co._SARL")
# game
rrem_folder(ROtarget + "\\_tmpEmblem")
shutil.rmtree(ROtarget + "\\.inn.meta.dir", ignore_errors=True, onerror = on_ro_error)
shutil.rmtree(ROtarget + "\\.inn.tmp.dir", ignore_errors=True, onerror = on_ro_error)
# usr profile temp
shutil.rmtree(ROtarget + "\\Frost\\.inn.meta.dir", ignore_errors=True, onerror = on_ro_error)
rrem_folder(ROtarget + "\\Frost")
#rrem_folder("R:\_games\rgROprime\Frost\.inn.meta.dir")

# files:
# game dump files (.dmp files)
dir_path = ROtarget
file_extenstion = '.dmp' # You can change it based on your need. 

for root, _, files in os.walk(dir_path):
    for file in files: 
        if file.endswith(file_extenstion): # for each file in the dir and the sub directories, if the file name ends with the '.exe'
            os.remove(os.path.join(root, file)) # Just delete it
            
# game log files (.log files)
dir_path = ROtarget + "\\gameManager"
file_extenstion = '.log' # You can change it based on your need. 

for root, _, files in os.walk(dir_path):
    for file in files: 
        if file.endswith(file_extenstion): # for each file in the dir and the sub directories, if the file name ends with the '.exe'
            os.remove(os.path.join(root, file)) # Just delete it
            
# game log files in Frost folder (.log files)
dir_path = ROtarget + "\\Frost"
file_extenstion = '.log' # You can change it based on your need. 

for root, _, files in os.walk(dir_path):
    for file in files: 
        if file.endswith(file_extenstion): # for each file in the dir and the sub directories, if the file name ends with the '.exe'
            os.remove(os.path.join(root, file)) # Just delete it
            
# game txt files in Frost folder (.txt files)
dir_path = ROtarget + "\\Frost"
file_extenstion = '.txt' # You can change it based on your need. 

for root, _, files in os.walk(dir_path):
    for file in files: 
        if file.endswith(file_extenstion): # for each file in the dir and the sub directories, if the file name ends with the '.exe'
            os.remove(os.path.join(root, file)) # Just delete it
            
# game screenshots files (.jpg files)
dir_path = ROtarget + "\\ScreenShot"
file_extenstion = '.jpg' # You can change it based on your need. 

for root, _, files in os.walk(dir_path):
    for file in files: 
        if file.endswith(file_extenstion): # for each file in the dir and the sub directories, if the file name ends with the '.exe'
            os.remove(os.path.join(root, file)) # Just delete it
            
#############################
#
# flush dns
os.system("ipconfig /flushdns")

#############################
#
# restart network
os.system("net stop hns")
os.system("net start hns")