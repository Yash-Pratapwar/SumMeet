from transformers import pipeline
file = open('transcripted_files/transcripted_file.txt', 'r')
text = file.read()
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
summary = summarizer(text, max_length = 200, min_length = 150)
a = summary[0]['summary_text']
with open('transcripted_files/sumarized_file.txt', 'w') as file:
        file.writelines(a)
print(a)

