import socket
import pyaudio

# Constants
HOST = 'Raspberry_Pi_1_IP'  # Replace with the server's IP address
PORT = 12345
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Create an audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

while True:
    data = stream.read(CHUNK)
    s.send(data)

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
s.close()
