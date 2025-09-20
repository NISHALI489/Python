""" 1. Generate 10 different vehicle speed samples using python provided samples should represent a sign wave
    2. Generate 10 random vehicle speed using a sign wave."""

"""Solution: 
   Based on numbers in python we have problem statements 10 different vehicle speed using look up table which 
   can store all signals for simulation
   
   formula for sin of 2*pi*fi/(fs)   -->Descrete sample
                      where fi is infomation signal frequency
                            fs is sampling frequency

    In typical vehicle maximun speed is 250km/hr
   """

#Start of program

import math
import random
#empty list
vehicleSpeed_samples = []
for rider in range(0,10):
    vehicleSpeed_samples.append(250*math.sin(2*math.pi*rider*1000/8000))
    print(vehicleSpeed_samples[rider])

random.random()