import asyncio
import websockets
from threading import Thread



async def echo(websocket, path):
    msg = await websocket.recv()
    print(msg)
    # print(path)
    # async for message in websocket:
    #     print(message,'received from client')
    #     greeting = f"Hello {message}!"
    #     await websocket.send(greeting)
    #     print(f"> {greeting}")

# def main():
loop = asyncio.get_event_loop()
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
loop.run_until_complete(websockets.serve(echo, '0.0.0.0', 8765))
loop.run_forever()

# Thread(target=main).start()