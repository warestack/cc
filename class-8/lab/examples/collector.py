import zmq

from common import RESULT_ENDPOINT, TASKS, lab_socket

with zmq.Context() as context, lab_socket(context, zmq.PULL) as socket:
    socket.bind(RESULT_ENDPOINT)
    print(f"PULL collector waiting on {RESULT_ENDPOINT}", flush=True)
    total = 0
    for _ in TASKS:
        result = socket.recv_json()
        total += result["number"]
        print(f"Received task {result['id']} from worker {result['worker']}: total={total}")
    print(f"Final total: {total}")
