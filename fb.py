#!/usr/bin/python
print "Content-Type: text/html\n\n"
import cgi, cgitb, os

from fbchat import Client
from fbchat.models import *
client = Client('juulythebear@gmail.com','JerryisA1')
user = client.searchForUsers('Jerry Ye')[0]

message_id = client.send(Message(text='I AM JUULY THE BEAR!Im going to take yo\
 ur JUULES!'), thread_id=user.uid, thread_type=ThreadType.USER)