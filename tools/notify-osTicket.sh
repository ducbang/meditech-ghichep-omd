#!/bin/bash
# osTicket Notify

SECRET="24B07C94FD38DE3D2C9A0311D84353C8"
DOMAIN="192.168.30.121"
if [ "$NOTIFY_WHAT" = "HOST" ]
then
		SUBJECT=$(echo -e "$NOTIFY_HOSTNAME - $NOTIFY_WHAT")
        INFO=$(echo -e "$NOTIFY_HOSTNAME \n $NOTIFY_WHAT: $NOTIFY_HOSTSTATE\nAt: $NOTIFY_DATE")
else
		SUBJECT=$(echo -e "$NOTIFY_HOSTNAME - $NOTIFY_WHAT: $NOTIFY_SERVICEDESC")
        INFO=$(echo -e "HOST: $NOTIFY_HOSTNAME \n $NOTIFY_WHAT: $NOTIFY_SERVICEDESC - $NOTIFY_SERVICEOUTPUT\nAt: $NOTIFY_DATE")
fi

curl -X POST -H "X-API-Key: $SECRET" -v -d'{"'"autorespond"'":false, "'"source"'": "'"API"'", "'"name"'": "'"GUEST"'", "'"email"'":"'"hoangdh@example.com"'", "'"subject"'":"'"$SUBJECT"'", "'"message"'":"'"$INFO"'", "'"topicId"'" : "'"2"'"}' http://$DOMAIN/helpdesk/api/http.php/tickets.json