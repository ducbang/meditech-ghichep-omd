#!/usr/bin/env python
'''
Slack - Zabbix Integration Webhook
A Slack incoming webhook to show events from Zabbix.

Usage: slack_zabbix.py <to> <subject> <message>

See the README for more information
'''

import json
import httplib2
import sys

##
########################################################
## only change below here if you know what you are doing
def usage():
    print "slack_zabbix.py <to> <subject> <message>\n\
    \n\
    <to>        channel or person\n\
    <subject>   subject line\n\
    <message>   message body\n\
    \n\
    example: slack_zabbix.py '#alerts' 'PROBLEM' 'Average ;; Zabbix server ;; Zabbix discoverer processes more than 75% busy ;; {TRIGGER.ID} ;; {EVENT.ID} ;; {EVENT.ID} ;; {ITEM.ID1} ;; {ITEM.NAME1}}'"

'''
Default subject: {TRIGGER.STATUS}
Default message: {TRIGGER.SEVERITY} ;; {HOST.NAME1} ;; {TRIGGER.NAME} ;; {TRIGGER.ID} ;; {EVENT.ID} ;; {ITEM.ID1} ;; {ITEM.NAME1} ;; {HOST.IP1} ;; {ITEM.DESCRIPTION1} ;; {ITEM.LASTVALUE1} ;; {EVENT.DATE} {TIME}
'''

def main():
    try:
        args = sys.argv[1:]
    except:
        usage()
        sys.exit(2)

    # parse command line input
    channel = args[0]
    status = args[1]
    result = args[2].split(' ;; ')
    severity = result[0]
    device = result[1]
    message = result[2]
    triggerid = result[3]
    eventid = result[4]
    itemid = result[5]
    itemname = result[6]
	deviceip = result[7]
	itemdes = result[8]
	itemvalue = result[9]
	eventtime = result[10]
    zabbixurl = args[3]
    botname = args[4]
    hookurl = args[5]
    zabbix_icon = args[6]
	
	# Display IP and Hostname

    summary = device + " (" + diachiip + "): " + status + ": " + message
    ack_url = zabbixurl + "/zabbix.php?action=acknowledge.edit&acknowledge_type=0&eventids[]=" + eventid + "&backurl=tr_events.php%3Ftriggerid%3D" + triggerid + "%26eventid%3D" + eventid

    imagelocal = '/usr/local/share/zabbix/alertscripts'
    # set the color based on severity
    if status == "OK":
        color = "good" #green
        thumb = imagelocal + "/img/ok.png"
    elif severity == "Disaster":
        color = "#FF3838"
        thumb = imagelocal + "/img/disaster.png"
    elif severity == "High":
        color = "#FF9999"
        thumb = imagelocal + "/img/high.png"
    elif severity == "Average":
        color = "#FFB689"
        thumb = imagelocal + "/img/average.png"
    elif severity == "Warning":
        color = "#FFF6A5"
        thumb = imagelocal + "/img/warning.png"
    elif severity == "Information":
        color = "#D6F6FF"
        thumb = imagelocal + "/img/information.png"
    elif severity == "Not classified":
        color = "#DBDBDB"
        thumb = ""
    else:
        color = ""
        thumb = ""

    if status == "PROBLEM":
        fields = [{
            "title": "Actions",
            "value": "<" + ack_url + "|Acknowledge> | <" + zabbixurl + "/tr_comments.php?triggerid=" + triggerid + "|Description> | <" + zabbixurl + "/history.php?action=showgraph&itemids[]=" + itemid + "|" + itemname + " Graph >",
            "short": True
        }]
    else:
        fields = [{}]

    attachment = [{
        "fallback": summary,
        "thumb_url": thumb,
        "text": message + ": " + itemdes + ": " + itemvalue + "\nTime: " + eventtime,
        "title": status + ": " + device + " (" + deviceip + ")",
        "title_link": zabbixurl + "/tr_events.php?triggerid=" + triggerid + "&eventid=" + eventid,
        "color": color,
        "fields": fields
    }]

    # post to slack
    payload = json.dumps({
        "username": botname,
        "icon_url": zabbix_icon,
        "channel": channel,
        "attachments": attachment
    })

    h = httplib2.Http()
    (resp, content) = h.request(hookurl, "POST", body=payload, headers={'content-type':'application/json'})

if __name__ == "__main__":
    main()

