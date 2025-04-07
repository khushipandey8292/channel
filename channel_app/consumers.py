from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("websocket connected...")
        self.send({
            "type": "websocket.accept"
        })
    def websocket_receive(self,event):
        print("Message received from client",event)   
        print(event['text'])
        self.send({
            "type":"websocket.sent",
            "text":"message sent to client"
        })
        
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
            "type":"websocket.sent",
            "text":"message sent to client"
        })
        
    async def websocket_disconnect(self,event):
        print("websocket Disconnected...",event)
        raise StopConsumer()