from twilio.rest import Client

account_sid = 'AC2e2e5625ee04bd4e4b01f76b670e8964'
auth_token = '61e03a29adf0f912fd6db682aaac8a5c'
client = Client(account_sid, auth_token)
def send_me():
 message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='HI my name is rishi',
  to='whatsapp:+917317506669'
)

 print(message.sid)