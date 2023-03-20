# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 15

# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
print('Recording...')
# Record audio for the given number of seconds
sd.wait()
print('Recording ended')
print('Recording saved to audio_files/recording1.wav')

#using wavio
# Convert the NumPy array to audio file
wv.write("audio_files/recording1.wav", recording, freq, sampwidth=2)