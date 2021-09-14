from twilio.rest import Client
account_sid ="AC35e5afb59d5e77987ece7986d1f4a661"
auth_token = "dfa1375b00d62d1328d174614286e252"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              to="+919926952072",
                              from_="+12082132722",
                              body="Hi there!"
                          )

print(message.sid)