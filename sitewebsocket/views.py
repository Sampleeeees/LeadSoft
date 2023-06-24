import asyncio
import threading
from asgiref.sync import sync_to_async
from django.shortcuts import render
from .models import Visit
import websockets


# Create your views here.
thread_a = None
info = 'server not started'

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
        print(message)
        await save_message(message)

async def save_message(message):
    spli = str(message).split(',')
    x = Visit()
    x.user_id = spli[0]
    x.url = spli[1]
    await sync_to_async(x.save)()

async def websocket_server():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

def start_websocket_server():
    asyncio.run(websocket_server())

def home(request):
    global thread_a, info
    obj = Visit.objects.all()
    if request.method == 'POST':
        post_filter = request.POST['filter']
        if post_filter == 'all':
            history = obj.order_by('-date')
        else:
            history = obj.filter(user_id=post_filter)
    else:
        history = obj.order_by('-date')
    return render(request, 'sitewebsocket/index.html', {'history': history, 'info': info})

if not thread_a:
    thread_a = threading.Thread(target=start_websocket_server)
    thread_a.start()


