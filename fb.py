from fbchat import Client
from fbchat.models import *
client = Client('juulythebear@gmail.com','JerryisA1')
user = client.searchForUsers('Eric Li')[0]

message_id = client.send(Message(text='I AM JUULY THE BEAR!Im going to take your JUULES!'), thread_id=user.uid, thread_type=ThreadType.USER)
