from pydub import AudioSegment

#importing file from location by giving its path
sound = AudioSegment.from_file("../audio_files/The_Internet_Said_So_EP158_seg1.mp3")

#duration calculation function
sound.duration_seconds == (len(sound) / 1000.0)
#seconds to minutes conversion
minutes_duartion = int(sound.duration_seconds // 60)
seconds_duration = round((sound.duration_seconds % 60))
print(minutes_duartion,':',seconds_duration)
mins = str(minutes_duartion)
secs = str(seconds_duration)
mins += secs
duration = int(mins)
print(duration)
print(type(duration))

# Selecting Portion we want to cut
StrtMin = 0
StrtSec = 0

EndMin = 0
EndSec = 30

# Time to milliseconds conversion
StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = EndMin*60*1000+EndSec*1000
print(StrtTime, EndTime)
# Opening file and extracting portion of it
extract = sound[StrtTime:EndTime]

# Saving file in required location
extract.export("../audio_files/short.mp3", format="mp3")

# new file portion.mp3 is saved at required location

