import asyncio

import websockets
from pyexpat.errors import messages


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello, server!"
        print(f'Send: {message}')
        await websocket.send(message)

        response = await websocket.recv()
        print(f'Response: {response}')

asyncio.run(client())