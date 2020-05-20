#Directories to save the raw and rpm data
RPM_dir="/home/pi/Documents/Running_Wheel_Data/RPM/"
RAW_dir="/home/pi/Documents/Running_Wheel_Data/Raw/"

#Set the number of cages
from num_cages import num_cages
ncages=num_cages()
if not ncages:
    exit()

#This function will query whether you want to print something every time an interrupt is detected
from show_detections import show_detections
show_detect=show_detections()
if not show_detect:
    exit()

#GPIO stands for general purpose input output, use them as interrupt pins on Raspberry Pi
import RPi.GPIO as GPIO

#Some useful functions for getting the current date and time for saving data 
from TimeFunctions import GetDate as GetDate
from TimeFunctions import now as now
from TimeFunctions import clock as clock

#Import numpy for arrays
import numpy as np


#Timenow and time old will be used to calculate rpm every second
timenow=now()
timeold=timenow
timer=timenow

#Initialize rotations at 0, will be used to calculate rpm
rotations = np.zeros(ncages, dtype=int)

variables = {}

with open("GPIO.txt") as f:
    for line in f:
        name, value = line.split("=")
        variables[name] = int(value)

Cage001=variables['Cage001'] 
Cage002=variables['Cage002']  
Cage003=variables['Cage003'] 
Cage004=variables['Cage004'] 

Cage005=variables['Cage005'] 
Cage006=variables['Cage006'] 
Cage007=variables['Cage007'] 
Cage008=variables['Cage008'] 

Cage009=variables['Cage009'] 
Cage010=variables['Cage010'] 
Cage011=variables['Cage011'] 
Cage012=variables['Cage012']

#List cage correspondence to GPIO pins
CageList = [Cage001,Cage002,Cage003,Cage004,Cage005,Cage006,Cage007,Cage008,Cage009,Cage010,Cage011,Cage012] 
Cages=CageList[:ncages] #The list of GPIO pins you're using


#Create a lookup table for the cages associated with the pin numbers, for file saving purposes
Cage2Num = {
    Cage001: "001",
    Cage002: "002",
    Cage003: "003",
    Cage004: "004",
    
    Cage005: "005",
    Cage006: "006",
    Cage007: "007",
    Cage008: "008",
    
    Cage009: "009",
    Cage010: "010",
    Cage011: "011",
    Cage012: "012",
}

#GPIO Pins will be used to detect when the voltage is pulled low and call the interrupt, "rotation_det"
GPIO.setmode(GPIO.BCM)
GPIO.setup(Cages, GPIO.IN, pull_up_down=GPIO.PUD_UP)



###################################################################################################################################
###################################################################################################################################

# This is called everytime the magnet passes the sensor. A time point will be saved in a textfile for each 24 hour period
def rotation_det(cage):  
    
    #Now function gives the date with year, month, day, hour, minute, second, microsecond
    (date,timepoint)=GetDate()
    filename=Cage2Num[cage] + "/RunningWheel" + Cage2Num[cage] +"_raw_"+date+".txt"
    
    if show_detect:
        print(Cage2Num[cage] + " Detected")

    global rotations #declare global rotations so it affects the variable outside this function
    cage_num = int(Cage2Num[cage]) -1
    rotations[cage_num]=rotations[cage_num]+1 #increase number of rotations by 1

    with open(RAW_dir + filename,'a') as file:
        file.write(timepoint+"\n")
            
for cage in Cages:
    GPIO.add_event_detect(cage,GPIO.FALLING, callback=rotation_det,bouncetime=50)


try:
    while True:
        timenow=now()
        
        if timenow-timer >=1: 
            print("...\n")
            timer=timenow
            
        elif timenow-timeold >= 5:
            
            #Calculate RPM for each cage by multiplying rotations in 5 seconds by 12       
            RPMs = rotations * 12
            clock()
            
            print ('RPMs:',RPMs,'\n')

            #Reset all rotations counters to zero
            rotations = np.zeros(ncages, dtype=int)

            timeold=timenow
            timer=timenow
            (date,timepoint)=GetDate()
    
            rawfilenames = [None] * ncages
            for iFile in range(0,ncages):
                rawfilenames[iFile] = str(iFile+1).zfill(3) + "/RunningWheel" + str(iFile+1).zfill(3) + "_rpm_" + date + ".txt"
                with open(RPM_dir + rawfilenames[iFile],'a') as file:
                    file.write(timepoint+": "+str(RPMs[iFile])+"\n")

                    
except KeyboardInterrupt:
    GPIO.cleanup() #clean up GPIO on exit
    
GPIO.cleanup() #clean up on button press exit

