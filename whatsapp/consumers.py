import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref import sync_to_async

class chatconsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        