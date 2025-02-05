from moviepy import *

clip = VideoFileClip("rolling.MOV")

clip = clip.resized(clip.size[::-1])

clip = clip.resized(0.2)

cropped_clip = clip.crop(x1=50, y1=50, x2=50, y2=250)

text1 = TextClip(
    font="Doto-Black.ttf",
    text="Rolling,",
    font_size=30,
    color=(0, 0, 0),
)

text2 = TextClip(
    font="Doto-Black.ttf",
    text="Rolling!!!",
    font_size=30,
    color=(0, 0, 0),
)

video_size = clip.size
text1_size = text1.size
text2_size = text2.size

print(video_size)
print(text1_size)
print(text2_size)

text1 = text1.with_position((int(video_size[0]/2 - text1_size[0]/2), int(video_size[1]/10))).with_duration(2)
text2 = text2.with_position((int(video_size[0]/2 - text2_size[0]/2), int(video_size[1]/10 + text1_size[1] + text1_size[1]/2))).with_duration(2)

output = CompositeVideoClip([clip, text1, text2])

output.write_gif('output.gif')