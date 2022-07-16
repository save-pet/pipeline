import os
from twilio.rest import Client

account_sid = ''
auth_token = ''
print(account_sid)

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="보이냐!22!",
    from_="+17657905252",
    to="+821027828277")

print(message.sid)

# VA5157fceea359962c32e8a0e7bd46a783