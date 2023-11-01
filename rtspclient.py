import cv2
import pyaudio
import numpy as np

if __name__ == "__main__":
    cap = cv2.VideoCapture("rtsp://<server_ip>:8554/live")

    # Audio configuration
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio_stream = pyaudio.PyAudio()
    audio_output = audio_stream.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Extract audio from the frame (you may need to adapt this part)
        audio_data = frame

        # Play audio
        audio_output.write(audio_data)

    cap.release()
    cv2.destroyAllWindows()
    audio_output.stop_stream()
    audio_output.close()
    audio_stream.terminate()
