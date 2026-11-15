import time

import zmq

from common import TASK_ENDPOINT, TASKS, lab_socket

with zmq.Context() as context, lab_socket(context, zmq.PUSH) as socket:
    socket.bind(TASK_ENDPOINT)
    print(f"PUSH producer listening on {TASK_ENDPOINT}", flush=True)
    time.sleep(1)  # Give the two waiting workers time to connect.
    for task_id, number in enumerate(TASKS, start=1):
        socket.send_json({"id": task_id, "number": number})
        print(f"Sent task {task_id}: {number}")
        time.sleep(0.15)
    print(f"Expected final total: {sum(TASKS)}")
