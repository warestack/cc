from argparse import ArgumentParser

import zmq

from common import REPLY_ENDPOINT, lab_socket

parser = ArgumentParser()
parser.add_argument("name", help="Your client label, for example A or B")
args = parser.parse_args()

with zmq.Context() as context, lab_socket(context, zmq.REQ) as socket:
    socket.connect(REPLY_ENDPOINT)
    for number in range(1, 4):
        socket.send_string(f"request {number} from {args.name}")
        print(f"Client {args.name} received: {socket.recv_string()}")
