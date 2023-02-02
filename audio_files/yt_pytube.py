# #Importing Pytube library
# import pytube
# # Reading the above Taken movie Youtube link
# video = 'https://www.youtube.com/watch?v=9MZY5tugc_Y'
# data = pytube.YouTube(video)
# # Converting and downloading as 'MP4' file
# audio = data.streams.get_audio_only()
# audio.download()
# importing packages
from pytube import YouTube
import os

# url input from user
yt = YouTube(
	str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
