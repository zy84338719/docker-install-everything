# ZeroMQ

ZeroMQ messaging library development environment.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your desired configuration
docker-compose up -d
```

## Usage

Enter the container and install pyzmq:

```bash
docker exec -it zeromq bash
pip install pyzmq
```

## Running Examples

Create Python scripts in the `conf/` directory (mounted as `/app` inside the container).

### Hello World Server (conf/hwserver.py)

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print(f"Received: {message}")
    socket.send(b"World")
```

### Hello World Client (conf/hwclient.py)

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send(b"Hello")
message = socket.recv()
print(f"Received: {message}")
```

Run inside the container:

```bash
# Terminal 1
python hwserver.py

# Terminal 2
python hwclient.py
```

## Notes

- The `conf/` directory is mounted as `/app` inside the container.
- Place your Python scripts in `conf/` to access them inside the container.
- The container stays running (`tail -f /dev/null`) so you can exec into it.
