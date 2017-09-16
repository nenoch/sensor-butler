import urllib2
import pir

while True:
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
        print('Not Connected yet')
    else:
        print('Connected to WiFi')
        pir.startSensor()
        exit()
