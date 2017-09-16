from gpiozero import MotionSensor
import json
import requests

pir = MotionSensor(4)
webhook_url = 'https://hooks.slack.com/services/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'
json_text = {'text':'Door :door: is open :open_hands:!'}

while True:
    print('Running')
    if pir.motion_detected:
        print('motion detected...')
        response = requests.post(
            webhook_url, data=json.dumps(json_text),
            headers={'Content-Type':'application/json'})
        if response.status_code != 200:
            print('Request to slack returned an error %s' % (response.status_code))
        exit()
