import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

def record_audio(filename, duration, samplerate=44100):
    
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording finished. Saving to file...")
    sf.write(filename, recording, samplerate)
    print(f"Audio saved to {filename}")

if __name__ == "__main__":
    record_audio("output.wav", 5, 44100)  # Record for 5 seconds and save to output.wav
    print("Recording complete. Check the output.wav file.")