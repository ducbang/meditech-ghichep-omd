#!/bin/bash
# SMS Notify by HoangDH
#######
#
# Register free account: https://speedsms.vn/sms-api/
#
########

SECRET="XXXXXXXXXXXXXXX"

if [ "$NOTIFY_WHAT" = "HOST" ]
then
        INFO=$(echo -e "$NOTIFY_HOSTNAME - $NOTIFY_WHAT: $NOTIFY_HOSTSTATE\nAt: $NOTIFY_DATE\n")
else
        INFO=$(echo -e "HOST: $NOTIFY_HOSTNAME - $NOTIFY_WHAT: $NOTIFY_SERVICEDESC - $NOTIFY_SERVICEOUTPUT\nAt: $NOTIFY_DATE\n")
fi

# Write to log file
echo "$NOTIFY_DATE - $NOTIFY_SERVICEDESC to $NOTIFY_CONTACTPAGER" >> /var/log/hoang-sms.log

curl -i -u "$SECRET:x" -H "Content-Type: application/json" -X POST -d "{\"to\": [\"$NOTIFY_CONTACTPAGER\"], \"content\": \"$INFO\", \"sms_type\": \"2\", \"sender\": \"\"}" http://api.speedsms.vn/index.php/sms/send