from argparse import ArgumentParser
import time

import zmq

from common import lab_socket

parser = ArgumentParser()
parser.add_argument("port", type=int)
args = parser.parse_args()
topics = ("cloud", "database", "api", "cloud")

with zmq.Context() as context, lab_socket(context, zmq.PUB) as socket:
    socket.bind(f"tcp://127.0.0.1:{args.port}")
    for number in range(1, 21):
        topic = topics[(number - 1) % len(topics)]
        message = f"{topic} {number} {args.port}"
        socket.send_string(message)
        print(f"Publishing: {message}", flush=True)
        time.sleep(0.25)
