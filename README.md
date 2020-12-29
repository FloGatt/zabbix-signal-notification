# zabbix-signal-notification

This is a little Zabbix alert script that uses bbernhard [signal-cli-rest-api](https://github.com/bbernhard/signal-cli-rest-api) in order to send Zabbix notifications to a predefined Signal account.

Place the script into the alertscripts folder of your Zabbix installation, make it executable and align the <sender> phone number in the script to your registered phone number.

On your Zabbix server, you have to create a custom Media type like shown below.

![Zabbix Media Type](https://github.com/FloGatt/zabbix-signal-notification/blob/MASTER/zabbix_media_type.png)
![Zabbix Media Type Templates](https://github.com/FloGatt/zabbix-signal-notification/blob/MASTER/zabbix_message_templates.png)


