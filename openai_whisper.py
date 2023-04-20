import whisper

def text_transcript(file_name):
    model = whisper.load_model("medium")
    result = model.transcribe('summeet_package/audio_files_uploaded/'+file_name+'.mp3', fp16=False, language = 'Hindi', task='translate')
    text = result["text"]
    print(result["text"])
    with open('summeet_package/transcripted_files/'+file_name+'.txt', 'w') as file:
            file.writelines(text)

