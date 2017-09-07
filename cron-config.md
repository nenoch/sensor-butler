In the terminal:
```
$ crontab -e

```
The first time you run crontab the system will ask which editr you'd like to use.
Select nano.

Copy and paste the following cron jobs at the end of the document:
```
@reboot python /home/pi/Desktop/sensor-butler/pir.py &

0 0 * * * python /home/pi/Desktop/sensor-butler/pir.py

```
The first line will run the script in the background at startup, the second will run the script at midnight everyday.
