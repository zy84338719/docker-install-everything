#!/usr/bin/env python3
"""
ZeroMQ Example Server
Demonstrates REQ/REP pattern on port 5555
"""

import zmq
import time
import sys

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("ZeroMQ server started on port 5555")
    sys.stdout.flush()

    while True:
        # Wait for next request from client
        message = socket.recv_string()
        print(f"Received request: {message}")

        # Do some work
        time.sleep(1)

        # Send reply
        socket.send_string(f"World from ZeroMQ")
        print("Sent reply")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
