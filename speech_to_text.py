#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('audio_files/result.wav') as source:
    
    audio_text = r.record(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google_cloud(audio_text)
        print('Converting audio transcripts into text ...')
        print('The text has been saved to transcripted_files/transcripted_file.txt')
        print('====================================================================')
        print('Transcripted text:\n',text)
        with open('transcripted_files/transcripted_file.txt', 'w') as file:
            file.writelines(text)
    
    except:
        print('Sorry.. run again...')