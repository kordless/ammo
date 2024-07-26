# Function Summary

# File: tunnel\client.py
def file_summary():
    imports = ['asyncio', 'websockets', 'json', 'inlets.client.InletsClient']
    decorators = []
    functions = ['start_inlets_client']
    function_calls = ['websockets.connect', 'print', 'websocket.recv', 'json.loads', 'print', 'InletsClient', 'client.connect', 'start_inlets_client', 'None.run_until_complete', 'asyncio.get_event_loop', 'connect_websocket']
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

# File: tunnel\server.py
def file_summary():
    imports = ['flask.Flask', 'flask.request', 'flask.jsonify', 'inlets.server.InletsServer', 'os', 'json', 'asyncio', 'websockets']
    decorators = []
    functions = ['receive_data']
    function_calls = ['Flask', 'set', 'asyncio.run', 'broadcast', 'json.dumps', 'jsonify', 'app.route', 'websocket.send', 'connected_clients.add', 'websocket.wait_closed', 'connected_clients.remove', 'websockets.serve', 'server.wait_closed', 'os.environ.get', 'InletsServer', 'inlets_server.run', 'None.run_until_complete', 'asyncio.get_event_loop', 'start_websocket_server', 'app.run']
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

