from transformers import pipeline
def text_summ(file_name):
    file = open('summeet_package/transcripted_files/'+file_name+'.txt', 'r')
    text = file.read()
    summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
    summary = summarizer(text, max_length = 200, min_length = 50)
    summ_text = summary[0]['summary_text']
    with open('summeet_package/summarized_files/'+file_name+'_summarized.txt', 'w') as file:
            file.writelines(summ_text)
    return summ_text


