import zmq

from common import REPLY_ENDPOINT, lab_socket

with zmq.Context() as context, lab_socket(context, zmq.REP) as socket:
    socket.bind(REPLY_ENDPOINT)
    print(f"REP server waiting on {REPLY_ENDPOINT}", flush=True)
    for _ in range(6):
        request = socket.recv_string()
        print(f"Server received: {request}")
        socket.send_string(f"reply to {request}")
