# -*- coding: utf-8 -*-
# Author : Xinyue Sun
# Time : 2022/11/02
# Description : calculate the number density of cations and anions, the input files are cacom and ancom in which the coordinate of ions are writed


from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Density_of_number():
    def __init__(self):
        self.x_min=0
        self.x_max=0
        self.y_min=0
        self.y_max=0
        self.z_min=0
        self.z_max=0
        self.volume=0

    def density_of_number(self,z_0,z_1,com_file):
        self.x_min=x_0
        self.x_max=x_1
        self.y_min=y_0
        self.y_max=y_1
        self.z_min=z_0
        self.z_max=z_1
        self.volume=(self.x_max-self.x_min)*(self.y_max-self.y_min)*(self.z_max-self.z_min)

        array=np.loadtxt(com_file)
        number=0
        density_of_number=0.0
        f=open("coord_in",'a')
        for i in range(len(array)):
            x=array[i,0]
            y=array[i,1]
            z=array[i,2]
            if (x>=self.x_min and x<=self.x_max) and (y>=self.y_min and y<=self.y_max) and (z>=self.z_min and z<=self.z_max):
                # print(x,y,z)
                number=number+1
        f.close()
        density_of_number=number/self.volume
        return density_of_number
file=input("please input the com file")
y_list = np.arange(-7,7,0.1).tolist()
for y in y_list:
    x_0 = float("-25.443")
    x_1 = float("24.565")
    y_0 = float(y)
    y_1 = float(y + 0.1)
    z_0=float("42")
    z_1=float("86")

    density_inst=Density_of_number()
    density_of_number=density_inst.density_of_number(z_0,z_1,file)
    print(density_of_number*2.15721)

