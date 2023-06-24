import asyncio
import websockets
from .models import Visit
import django
from asgiref.sync import sync_to_async


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message)
        spli = str(message).split('-')
        x = Visit()
        x.user_id = spli[0]
        x.url = spli[1]
        await sync_to_async(x.save)()


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever


django.setup()
asyncio.run(main())