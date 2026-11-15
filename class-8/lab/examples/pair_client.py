import zmq

from common import PAIR_ENDPOINT, lab_socket

with zmq.Context() as context, lab_socket(context, zmq.PAIR) as socket:
    socket.connect(PAIR_ENDPOINT)
    for number in range(1, 6):
        print(f"Client received: {socket.recv_string()}")
        socket.send_string(f"client reply {number}")
