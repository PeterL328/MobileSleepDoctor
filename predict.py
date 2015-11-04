import sys
import pycurl
import json
import requests
import pprint

with open('data.csv','r') as payload:
   mypayload = {'file' : payload}
   mydata = {"service_name" : "joint-test5",
           "apikey" : "YOUR API KEY"
            }
   r = requests.post("https://api.havenondemand.com/1/api/sync/predict/v1", data = mydata, files=mypayload)
   r_dict = json.loads(r.text)

   abp = r_dict['values'][0]['row'][-1]


'''if (len(sys.argv) == 3):    //assume 1 param only (x+1)
   total_time_slept = sys.argv[1]
   file_path = sys.argv[2]
'''

if (total_time_slept > 12): 
    sleep_message = "Too much sleep!"
elif (total_time_slept >= 7.5): 
    sleep_message = "Perfect amount of sleep!"
else: 
    sleep_message = "You need more sleep!"


line1 ='Good Morning! '
line2 ='Total Time Slept: '
line3 ='Average Body Position: '
line4 ='Health Warning: '
line5 ='By the way: '

from twilio.rest import TwilioRestClient
ACCOUNT_SID = 'YOUR ACCOUNT ID'
AUTH_TOKEN = 'YOUR AUTH TOKEN'
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

str_body = line1 + '\n' + line2 + str(total_time_slept) + '\n' + line3 + str(abp) + '\n'

if abp == 'starfish':
    str_body += line4 + 'Snoring, may casue sleep apnea' + '\n'
elif abp == 'free fall':
    str_body += line4 + 'Reduced oxygen intake, Neck pain and Body Ache' + '\n'
elif abp == 'soldier':
    str_body += line4 + 'Blocks airway to body, may cause sleep apnea' + '\n'
elif abp == 'log':
    str_body += line4 + 'Neck pain, Hip pain due to spine rotation' + '\n'
else:
    str_body += 'No detected Average Body Position' + '\n'

str_body += line5 + str(sleep_message)

client.messages.create(to='THE NUMBER TO SENT TO',
                       from_='TWILIO NUMBER GOES HERE',
                       body = str_body)
