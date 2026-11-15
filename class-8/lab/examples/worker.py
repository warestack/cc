from argparse import ArgumentParser

import zmq

from common import RESULT_ENDPOINT, TASK_ENDPOINT, lab_socket

parser = ArgumentParser()
parser.add_argument("name", help="Your worker label, for example A or B")
args = parser.parse_args()

with zmq.Context() as context:
    with lab_socket(context, zmq.PULL) as incoming, lab_socket(context, zmq.PUSH) as outgoing:
        incoming.connect(TASK_ENDPOINT)
        outgoing.connect(RESULT_ENDPOINT)
        print(f"Worker {args.name} waiting for tasks", flush=True)
        while True:
            task = incoming.recv_json()
            outgoing.send_json({**task, "worker": args.name})
            print(f"Worker {args.name} processed task {task['id']}", flush=True)
