from youtube_transcript_api import YouTubeTranscriptApi

# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")

# prints the result
# print(srt)
with open('transcripted_files/yt_transcript.txt', 'a') as file:
    for dict_item in srt:
        text = dict_item['text']
        file.writelines(text+'\n')
