import sounddevice as sd
import socket
import numpy as np

# Configuration
receiver_ip = '192.168.1.101'  # Laptop 1's IP address
receiver_port = 12345
sample_rate = 44100

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((receiver_ip, receiver_port))

# Initialize audio stream
def audio_callback(outdata, frames, time, status):
    if status:
        print(status, flush=True)
    data, addr = sock.recvfrom(outdata.nbytes)
    outdata[:] = np.frombuffer(data, dtype=np.int16)

with sd.OutputStream(callback=audio_callback, channels=2, samplerate=sample_rate):
    print(f"Receiving audio from {receiver_ip}:{receiver_port}")
    sd.sleep(-1)
