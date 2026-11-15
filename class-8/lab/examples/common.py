from contextlib import contextmanager

import zmq

PAIR_ENDPOINT = "tcp://127.0.0.1:5555"
REPLY_ENDPOINT = "tcp://127.0.0.1:5556"
TASK_ENDPOINT = "tcp://127.0.0.1:5559"
RESULT_ENDPOINT = "tcp://127.0.0.1:5560"
TASKS = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)


@contextmanager
def lab_socket(context, socket_type):
    """Give each example a bounded wait and close its socket on exit."""
    with context.socket(socket_type) as socket:
        socket.rcvtimeo = 60_000
        socket.sndtimeo = 60_000
        socket.linger = 1_000
        try:
            yield socket
        except zmq.Again:
            raise SystemExit("Timed out waiting for messages or a peer. Check the other terminals and rerun.") from None
        except KeyboardInterrupt:
            raise SystemExit("Stopped.") from None
