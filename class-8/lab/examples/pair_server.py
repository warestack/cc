import zmq

from common import PAIR_ENDPOINT, lab_socket

with zmq.Context() as context, lab_socket(context, zmq.PAIR) as socket:
    socket.bind(PAIR_ENDPOINT)
    print(f"PAIR peer waiting on {PAIR_ENDPOINT}", flush=True)
    for number in range(1, 6):
        socket.send_string(f"server message {number}")
        print(f"Server received: {socket.recv_string()}")
