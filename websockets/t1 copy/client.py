import asyncio
import websockets
from threading import Thread

URI = 'ws://localhost:8765'
# URI = 'ws://192.168.1.10:7000'

async def hello(str):
    async with websockets.connect(uri) as websocket:
        await websocket.send(str)
        # print(f"(client) send to server: Jimmy")
        # name = await websocket.recv()
        # print(f"(client) recv from server {name}")

def send(str):
    loop.run_until_complete(hello(URI))

def main():
    # loop = asyncio.get_event_loop()
    loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    loop.run_until_complete(hello(URI))

thread = Thread(target=main)
thread.start()
print('start')
thread.join()
print('join')