import librosa
import numpy as np

def find_hits(recording, samplerate):
    starts = librosa.onset.onset_detect(y=recording, sr=samplerate, units="samples")
    window = int(samplerate * 0.05)
    hits = []

    for start in starts:
        end = start + window
        if end > len(recording):
            end = len(recording)
        hits.append(recording[start:end])
    
    #return hits
    for i, h in enumerate(hits):
        print(i, np.abs(h).max())
#def extract_features(hit, samplerate):
        
    