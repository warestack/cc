from argparse import ArgumentParser

import zmq

from common import lab_socket

parser = ArgumentParser()
parser.add_argument("ports", type=int, nargs="+")
args = parser.parse_args()

messages_left = dict.fromkeys(args.ports, 3)
with zmq.Context() as context, lab_socket(context, zmq.SUB) as socket:
    socket.setsockopt_string(zmq.SUBSCRIBE, "cloud ")
    for port in messages_left:
        socket.connect(f"tcp://127.0.0.1:{port}")
    print("SUB waiting for three cloud messages per publisher", flush=True)

    while any(messages_left.values()):
        message = socket.recv_string()
        _, _, port_text = message.split()
        port = int(port_text)
        if messages_left[port] > 0:
            print(f"Subscriber received: {message}", flush=True)
            messages_left[port] -= 1
