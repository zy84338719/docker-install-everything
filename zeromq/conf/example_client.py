#!/usr/bin/env python3
"""
ZeroMQ Example Client
Demonstrates REQ/REP pattern connecting to port 5555
"""

import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://zeromq:5555")

    print("ZeroMQ client connected")

    for request in range(10):
        print(f"Sending request {request} ...")
        socket.send_string("Hello")

        # Get the reply
        message = socket.recv_string()
        print(f"Received reply {request} [ {message} ]")

if __name__ == "__main__":
    main()
