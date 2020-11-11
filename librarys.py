# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:43:56 2020

@author: UseR
"""

import os
import matplotlib.pyplot as plt
import math
from PIL import Image
import numpy as np


def plot_images(images):
    
    #plots the images in the list images
    li=os.listdir('C:/pictures')#list of the pictures names
    f ,axs = plt.subplots(len(images))
    for i in range(len(images)):
        axs[i].set_title(li[i])
        axs[i].imshow(images[i]) #imshow is from import matplotlib
    plt.show()
    


def transfer(path1,path2):
    
    li=os.listdir(path2)
    if (path1==createlibrary(createlibrary("C:/pythonfolder","folder"), "train")):#if its train library then only send 70% of the pictures
        for i in range(math.floor(0.7*len(li))):
            im=Image.open(os.path.join(path2, li[i]))# takes the path and the name of the picture and return Image object 
            im.save(os.path.join(path1, li[i]), 'jpeg')#saves the picture to the library
    if (path1==createlibrary(createlibrary("C:/pythonfolder","folder"), "test")):#if its test library send all the pictures
        for i in  li:
           im=Image.open(os.path.join(path2, i))
           im.save(os.path.join(path1, i), 'jpeg')
           
    
def createlibrary(path,name):
    if(path==''):#if theres no input, goes automatically to desktop
        path="C:/Users/UseR/Desktop"
    path=path+'/'+name
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    return path
createlibrary(createlibrary("C:/pythonfolder","folder"), "train")
createlibrary(createlibrary("C:/pythonfolder","folder"), "test")
createlibrary(createlibrary("", "folder"), "train")
createlibrary(createlibrary("", "folder"), "test")
folderName = createlibrary("C:/pythonfolder","folder")
p=createlibrary(createlibrary("C:/pythonfolder","folder"), "test")
transfer(p,'C:/pictures')

li=os.listdir(createlibrary(createlibrary("C:/pythonfolder","folder"), "test"))
images = [np.array(Image.open(os.path.join(createlibrary(createlibrary("C:/pythonfolder","folder"), "test"),filename))) for filename in li]
plot_images(images)



