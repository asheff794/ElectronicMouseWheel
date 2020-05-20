# ElectronicMouseWheel
An electronic mouse wheel for tracking activity of mice over time. A small neodymium magnet is attached to a mouse wheel, and a hall effect sensor logs the time during each pass of the magnet. This cannot differentiate the direction the mouse is running, but works for purposes of general activity tracking. While this code theoretically works with up to 12 cages, I've only tested it on 4 simultaneously. Too many cages may cause wheel rotations to be missed if they happen too close in time, this would require testing. I performed this work as a technician in Gloria Choi's lab at MIT.


#### Necessary Components
* Raspberry Pi
* Mouse Wheel (I used the Kaytee Silent Spinner Exercise Wheel - Mini) 
* US5881 Hall Effect Sensor
* Neodymium magnet (D7H2, K&J Magnetics)



### Electronics Setup
![US5881 Hall Effect Sensor Pins](https://github.com/asheff794/ElectronicMouseWheel/blob/master/US5881.PNG)

The datasheet for the hall US5881 Hall EFfect Sensor can be found here (https://cdn-shop.adafruit.com/datasheets/US5881_rev007.pdf). Pin 1 is connected to voltage, pin 2 to ground, and pin 3 will be our output. The voltage of pin 3 will be high at baseline, and drop when the south pole of a magnet is placed nearby. The raspberry pi will detect such drops in voltage that correspond to one rotation of the wheel. 

First, wire the hall effect sensors to the raspberry pi as below. 

### Running Software



## Authors

* **Alec Sheffield** (https://github.com/asheff794, contact with any questions at alec.g.sheffield@gmail.com)

