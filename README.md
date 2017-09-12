# Sensor Butler
![Sensor Butler Icon](./imgs/sensor-butler.png)   

##### _A Raspberry Pi device to share a message on a slack channel when the door is opened._

![Raspberry Pi & PIR sensor](./imgs/IMG_6392.JPG)  

**1) Slack & Webhooks**    
Create a slack team for prototyping purposes and your first slack App. You will need a incoming webhook url to send the POST request with your message to slack.  
https://api.slack.com/tutorials/slack-apps-hello-world  

Try out your incoming webhook in the terminal:
```
curl -X POST -H 'Content-type: application/json' --data '{"text":"Door :door: is open! :open_hands:"}' https://hooks.slack.com/services/YOUR-SLACK-WEBHOOK
```
**2) Raspberry Pi and PIR (passive infrared) motion sensor**  

Build your Raspberry Pi device. You will need:
* Raspberry Pi
* PIR sensor  
* PIR sensor  
* Jumper wires
* Dupont Wire
* Breadboard

_For easy setup_
* USB Wi-Fi adaptor
* USB Bluetooth adaptor

![wiring detail 1](./imgs/IMG_6393.JPG) | ![wiring detail 2](./imgs/IMG_6394.JPG)
------------ | -------------
![wiring detail 3](./imgs/IMG_6395.JPG) | ![wiring detail 4](./imgs/IMG_6396.JPG)

https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04
https://www.raspberrypi.org/learning/parent-detector/worksheet/

**3) Download the python script in your RPi**  
Download pir.py and change the webhook url to the one of your slack app.

**4) Schedule tasks with Cron**  
Follow the instruction in the cron-config.md file and the link below.
With this setting the sensor will be active at reboot and then everyday after midnight. Remember that the sensor will be 'triggerable' only once per day.   
_Note: change the path to the path of the pir.py script on your RPi_
https://www.raspberrypi.org/documentation/linux/usage/cron.md

### Further Resources

*Run the python script at startup (RPi)*   
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

*git on Raspberry Pi*   
https://projects.raspberrypi.org/en/projects/getting-started-with-git

*Self-updating apps using Docker*   
https://medium.com/imont/self-updating-iot-apps-on-the-raspberry-pi-using-docker-a0b223fd4eeb
