import socket
import pyaudio

# Constants
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# Accept a connection
conn, addr = s.accept()
print(f"Connected by {addr}")

# Create an audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

while True:
    data = conn.recv(CHUNK)
    stream.write(data)

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
s.close()
