#Exampl:
#021-10-26 10:26:44 | https://website.com/home | SUCCESS | Message
#2021-10-26 10:26:54 | https://website.com/about | SUCCESS | Message
#2021-10-26 10:27:01 | https://website.com/page | ERROR | Message
#2021-10-26 10:27:03 | https://website.com/user/me | SUCCESS | Message
#2021-10-26 10:27:04 | https://website.com/settings/ | ERROR | Message

import json

file_name = "log.txt"
file = open(file_name, "r")
data = []
order = ["date", "url", "type", "message"]

for line in file.readlines():
    details = line.split("|")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(order, details)}
    data.append(structure)
    
for entry in data:
    print(json.dumps(entry, indent = 4))

""" output format
{
    "date": "2021-10-20 10:26:44",
    "url": "https://website.com/home",
    "type": "SUCCESS",
    "message": "Message"
}
{
    "date": "2021-10-20 10:26:54",
    "url": "https://website.com/about",
    "type": "SUCCESS",
    "message": "Message"
}
{
    "date": "2021-10-20 10:27:01",
    "url": "https://website.com/page",
    "type": "ERROR",
    "message": "Message"
}
{
    "date": "2021-10-20 10:27:03",
    "url": "https://website.com/user/me",
    "type": "SUCCESS",
    "message": "Message"
}
{
    "date": "2021-10-20 10:27:04",
    "url": "https://website.com/settings/",
    "type": "ERROR",
    "message": "Message"
}
"""