import sounddevice as sd
import soundfile as sf
from Features import find_hits
import numpy as np
import librosa
import matplotlib.pyplot as plt

class Calibration:

    def __init__(self, samplerate, hits_per_type):
        self.samplerate = samplerate      
        self.noise_floor = None
        self.hits_per_type = hits_per_type

    def record_hits(self, hit_type, duration):
        print(f"Play {hit_type} {self.hits_per_type} times")
        recording = sd.rec(int(duration * self.samplerate), samplerate=self.samplerate, channels=1)
        sd.wait()
        recording = recording.flatten()
        return recording

if __name__ == "__main__":
    calibrator = Calibration(samplerate=44100, hits_per_type=5)
    recording = calibrator.record_hits("don", 10)
    hits = find_hits(recording, 44100)
    
    starts_sec = librosa.onset.onset_detect(y=recording, sr=44100, units="time")
    print(starts_sec)

    #loudness per detection
    for i, h in enumerate(hits):
        print(i, round(float(np.abs(h).max()), 3))

    #plot
    starts = librosa.onset.onset_detect(y=recording, sr=44100, units="samples")
    plt.plot(recording)
    for s in starts:
        plt.axvline(s, color="red")
    plt.show()
   




