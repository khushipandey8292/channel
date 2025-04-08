from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("websocket connected...",event)
        self.send({
            "type": "websocket.accept"
        })
    def websocket_receive(self,event):
        print("Message received from client",event)   
        print(event["text"])
        for i in range(10):
            self.send({
                "type":"websocket.send",
                "text":str(i)
            })
            sleep(1)   
    def websocket_disconnect(self,event):
        print("websocket Disconnected...",event)
        raise StopConsumer()
    
    
class MyAsyncConsumer(AsyncConsumer):
    async  def websocket_connect(self,event):
        print("websocket connected...")
        await self.send({
            "type": "websocket.accept"
        })
        
    async def websocket_receive(self,event):
        print("Message received from client",event)   
        print(event['text'])
        await self.send({
            "type":"websocket.send",
            "text":"message sent to client"
        }) 
        
    async def websocket_disconnect(self,event):
        print("websocket Disconnected...",event)
        raise StopConsumer()
