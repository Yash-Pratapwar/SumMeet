from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=cST_Q5VpLRw")
yt = yt.get('mp4', '360p')
yt.download('videos')