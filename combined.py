# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:45:31 2021

@author: cco004
"""

# An input code that prints in command line which function to plot 
# and allow to select a plot from the list 
# (option 1, plot 1, option2, plot 2, option 3 return

import matplotlib.pyplot as plt
import numpy as np

def plotletter(c):    
    c = input("Please enter a letter: ")
    plt.text(0.5, 0.7, c, size=50, rotation=00.,
        ha="center", va="center",
        bbox=dict(boxstyle="round",
                  ec=(1., 0.5, 0.5),
                  fc=(1., 0.8, 0.8),
                       )
             )
    plt.show()


"""
Created on Wed Jan 27 18:19:49 2021

@author: snc001
"""
import matplotlib.pyplot as plt
# from planar import BoundingBox


def PlotLetter(Z):
    plt.text (0.6, 0.7, Z, size = 50, rotation = 45,
            ha = "center", va = "center",
            bbox = dict(boxstyle = "round",
                        ec = (1., 0.5, 0.5),
                        fc = (1., 0.8, 0.8),
                        )
            )
    plt.show()        

decision = float(input('Please select an option: 1, 2 or 3: '))

while decision != 1 and decision !=2:
    print("You selected 3. No function returns")
    decision = float(input('Please select an option: 1, 2 or 3: '))

if decision == 1:
    print("You selected 1, take a look at the plot")
    # MyfunctionSine(100,1)1
elif decision == 2:
    print("You selected 2")
    plotletter("letter plot")

    
    

    
    
    