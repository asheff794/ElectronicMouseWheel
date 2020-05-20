# ElectronicMouseWheel
An electronic mouse wheel for tracking activity of mice over time. A small neodymium magnet is attached to a mouse wheel, and a hall effect sensor logs the time during each pass of the magnet. This cannot differentiate the direction the mouse is running, but works for purposes of general activity tracking. While this code theoretically works with up to 12 cages, I've only tested it on 4 simultaneously. Too many cages may cause wheel rotations to be missed if they happen too close in time, this would require testing. I performed this work as a technician in Gloria Choi's lab at MIT.


#### Necessary Components
* Raspberry Pi [Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* Mouse Wheel (I used the Kaytee Silent Spinner Exercise Wheel - Mini from [Chewy](https://www.chewy.com/kaytee-silent-spinner-small-animal/dp/128956)) 
* US5881 Hall Effect Sensor [Digikey](https://www.digikey.com/product-detail/en/melexis-technologies-nv/US5881LUA-AAA-000-BU/US5881LUA-AAA-000-BU-ND/431876?utm_adgroup=Sensors%20%26%20Transducers&utm_source=google&utm_medium=cpc&utm_campaign=Dynamic%20Search&utm_term=&utm_content=Sensors%20%26%20Transducers&gclid=CjwKCAjwqpP2BRBTEiwAfpiD-wNSWx2GdXjBr7UFpQpFPSFj9fMRnZgtkew62IWfcmn7tvfhYuWmuBoCIAoQAvD_BwE)
* Neodymium magnet [D7H2, K&J Magnetics](https://www.kjmagnetics.com/proddetail.asp?prod=D7h2)



### Electronics Setup
![US5881 Hall Effect Sensor Pins](https://github.com/asheff794/ElectronicMouseWheel/blob/master/US5881.PNG)

The datasheet for the hall US5881 Hall EFfect Sensor can be found here (https://cdn-shop.adafruit.com/datasheets/US5881_rev007.pdf). Pin 1 is connected to voltage, pin 2 to ground, and pin 3 will be our output. The voltage of pin 3 will be high at baseline, and drop when the south pole of a magnet is placed nearby. The Raspberry Pi will detect such drops in voltage that correspond to one rotation of the wheel. 

![Raspberry Pi GPIO Pins](https://github.com/asheff794/ElectronicMouseWheel/blob/master/Raspberry%20Pi%20Pins.png)

Raspberry Pi 3 and 4 have 40 GPIO (General Purpose Input Output) pins. I used a breadboard to keep wiring tidy. 

1. Connect 5V and Ground on the Raspberry Pi to the positive and negative rail on the breadboard respectively. 
2. Connect the positive rail of the breadboard to pin 1 of all US5881 Hall Effect Sensors.
3. Connect the negative rail of the rbeadboard to pin 2 of all US5881 Hall Effect Sensors.
4. Connect pin 3 of the 4 US5881 Hall Effect Sensors to GPIO 4,17,27, and 22 on the Raspberry Pi. This will correspond to cages 1-4. The correspondence between GPIO Pin and Cage # is found in GPIO.txt and can be changed if you like, but must be consistent with your wiring.

### Software Setup
1. Save the folder Running_Wheel somewhere in your Raspberry Pi. I saved it in Documents/Python_Scripts
2. Open the command prompt and navigate to the location of this folder using the following command (replace Documents/Python Scripts with the location of your Running_Wheel folder)
  >cd('Documents/Python Scripts/Running_Wheel)
3. Type in the following command to start the program.
  >python3 runningwheel.py
4. Two prompts will pop up.
    -Enter the number of cages:
    -Would you like to display detections?
    
The first question is the number of cages you are running the system on. I entered 4. The second prompt is asking whether you want something printed to the screen every time a wheel rotation is detected. This is used for initial troubleshoot, so type 'yes' for now.
 
 5. The system will begin running and output the RPMs of each cage every 5 seconds, along with the current time. Since you selected yes to "Would you like to display detections?", text will be printed every time a magnet passes a sensor.
 6. With the system running, test passing the magnets by the sensors so that they are successfully detected. The sensors only detect the south pole of the magnet, so make sure you know which side of the magnet is south before attaching it to the wheel.
 7. To stop the system, type Control C on the Raspberry Pi.
 
 ### Wheel Assembly

 1. Now that you know which side of the magnet is south, tape/glue the magnet to the running wheel so the south side is facing outside the cage. 
 
 2. Tape/glue the US5881 sensors to the cages with text facing towards the running wheel. Make sure the sensor and wheel are lined up so that when the wheel rotates, the magnet passes the sensor.
 
 
### Output
Congratulations, you now have an electronic mouse wheel for tracking the activity of your mice. Once you run the system, a new folder will appear in your Raspberry Pi's documents titled Running_Wheel_Data, containing two more folders Raw and RPM. In both Raw and RPM, there will be folders corresponding to all of your cages, containing text files for each day of data. For Cage 001 on January 1st, 2020, the text files will be RunningWheel001_raw_01_01_2020 and RunningWheel001_rpm_01_01_2020. In raw files, each line of the text file will have a timestamp of a single rotation in the format MM_DD_YYYY followed by the number of seconds since midnight. I found the data displayed in this manner convenient for analysis, though YMMV. RPM files will have a similar timestamp followed by the RPM for that 5 second interval. See the video below to see an example of the wheel and code in action.
  


## Potential Updates
  -Change output format of date and timestamp
  
  -Upload code to analyze output

## Authors

* **Alec Sheffield** (https://github.com/asheff794, contact with any questions at alec.g.sheffield@gmail.com)

