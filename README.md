# raspberry_pi
#We use a standard laptop to SSH into a raspberry pi for easy display access. 

#A breadboard using connecting wires, two resistors, two LEDs (for feedback), a capacitor (connected to the ground rail) connect the raspberri pi to the light sensor. The light sensor detects changes in light.

#Lightsensor.py collects signal from the sensor so that lighting typically produces a light sensor value below 100,000. Reading are taken every 5 seconds and printed in the terminal. When a shadow disrupts this general lighting the sensor value will invariably supersede 100,000 - typically this value will be ~300,000. Project.py will activate the camera.py program - which takes a picture - the moment the light sensor signal supersedes 100,000. Camera.py stores the picture in the home folder. After activating the camera.py program it will activate the mail.py program which attaches the picture taken and sends the email over to the email adress specified in mail.py. A record of these transactions - a value above 100,000, taking the picture, emailing the picture - are printed on the terminal as the light is disrupted.
