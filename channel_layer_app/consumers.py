from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
class RoomSyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket Connected..',event)
        print("channel Layer...",self.channel_layer)
        print("channel Name...",self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name...",self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        
        self.send({
            'type': "websocket.accept"
        })
    def websocket_receive(self,event):
        print("Message received from client",event['text']) 
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type':'chat.message',
            'message':event['text']
        })  
    def chat_message(self, event):
        print(event['message'])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    def websocket_disconnect(self,event):
        print("websocket Disconnected...",event)
        print("channel Layer...",self.channel_layer)
        print("channel Name...",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        raise StopConsumer()
    