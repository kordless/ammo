import asyncio
import websockets
import json
from inlets.client import InletsClient

async def connect_websocket():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            print(f"Received data: {data}")

def start_inlets_client():
    client = InletsClient(
        remote="localhost:8080",
        token="your-secret-token",
        upstream="http://localhost:8000"
    )
    client.connect()

if __name__ == "__main__":
    # Start Inlets client
    start_inlets_client()

    # Start WebSocket client
    asyncio.get_event_loop().run_until_complete(connect_websocket())