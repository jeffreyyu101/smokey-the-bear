import cgi,cgitb
cgitb.enable()
from fbchat import Client
from fbchat.models import *
client = Client('juulythebear@gmail.com','JerryisA1')
user = client.searchForUsers(ID)[0]

message_id = client.send(Message(text="Hi! I'm Juuly The Bear. I am messaging you to tell you that you are on notice for Juuling too much. Using our advanced machine learning software, we have deduced this. Please take notice. Juuling is extremely bad for your health. We would like you to give it up."), thread_id=user.uid, thread_type=ThreadType.USER)
