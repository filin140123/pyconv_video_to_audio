import moviepy.editor as mp
name = input("Enter video name with ext: ")
clip = mp.VideoFileClip(name).subclip(0, 4116)
clip.audio.write_audiofile(f"audio-{name.split('.')[0]}.mp3")
