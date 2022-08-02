
#Json is used for formatting our payload, requests is used for sending http request.
import requests, json

#Next we need to define a webhook URL. Desination URL that we send our webhook to.

#This is a site that generates webhooks: https://webhook.site
#Alex's unique Webhook URL:
webhook_url = 'https://webhook.site/dc3e2823-344f-4702-8cba-8d28191f3762'

#JSON formatted data:
data = {'name': 'jotforms spreadsheed',
        'Jotforms URL': 'https://form.jotform.com/210496156612050'}

#generate request object (this sends information)
#here we are sending information. We then set http headers as json
r = requests.post(webhook_url,data=json.dumps(data), headers={'Content-Type': 'application/json'})

#if this worked, the webhook was created. You can confirm by going to the webhook site
#which will have automatically refreshed. You should be able to see the request details.
#We have successfully sent a webhook to a webhook server.
