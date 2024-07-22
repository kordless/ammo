from flask import Flask, request, jsonify
from inlets.server import InletsServer
import os
import json
import asyncio
import websockets

app = Flask(__name__)
connected_clients = set()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    asyncio.run(broadcast(json.dumps(data)))
    return jsonify({"status": "received"}), 200

async def broadcast(message):
    for websocket in connected_clients:
        await websocket.send(message)

async def handle_client(websocket, path):
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)

async def start_websocket_server():
    server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    await server.wait_closed()

if __name__ == '__main__':
    # Start the Inlets server
    token = os.environ.get('INLETS_TOKEN', 'your-secret-token')
    inlets_server = InletsServer(token=token)
    inlets_server.run()

    # Start WebSocket server
    asyncio.get_event_loop().run_until_complete(start_websocket_server())

    # Run the Flask app
    app.run(host='0.0.0.0', port=8000)