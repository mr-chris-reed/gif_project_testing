from moviepy import *

clip = VideoFileClip("moxie.MP4")

clip = clip.resized(clip.size[::-1])

clip = clip.resized(0.2)

clip = clip.cropped(x1=0, y1=35, x2=200, y2=250)

text1 = TextClip(
    font="FontdinerSwanky-Regular.ttf",
    text="Moxie!",
    font_size=30,
    color=(0, 0, 0),
)

video_size = clip.size
text1_size = text1.size

print(video_size)
print(text1_size)

text1 = text1.with_position((int(video_size[0]/2 - text1_size[0]/2), int(video_size[1]/10))).with_duration(2)

output = CompositeVideoClip([clip, text1])

output = output.with_speed_scaled(2)

output.write_gif('output.gif')