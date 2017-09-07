### Crontab and Cron Jobs

In the terminal:
```$ crontab -e```

The first time you run crontab the system will ask which editor you'd like to use.
Select ```nano```.

Copy and paste the following cron jobs at the end of the document:
```
@reboot python /home/pi/Desktop/sensor-butler/pir.py &

0 0 * * * python /home/pi/Desktop/sensor-butler/pir.py
```

The 1st line will run the script in the background at startup, the 2nd will run the script at midnight everyday.
