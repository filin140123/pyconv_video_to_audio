import moviepy.editor as mp
from math import ceil

name = input("Enter video name with ext: ")
clip = mp.VideoFileClip(name)

start_input = input("Start encoding with this time (mm:ss): ")
m, s = [int(i) for i in start_input.split(":")]
start_seconds = m * 60 + s
end_seconds = ceil(clip.duration)

outclip = clip.subclip(start_seconds, end_seconds)
outclip.audio.write_audiofile(f"audio-{name.split('.')[0]}.mp3")
