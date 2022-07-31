import json
import os
import time

import PIL.Image
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.fx.resize import resize
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def filter_image(image_folder_path):
    images = [f"{image_folder_path}\\{path}" for path in os.listdir(image_folder_path)]

    image = []
    for i in range(len(images)):

        file_name = images[i].split("\\")[-1]
        if file_name.endswith('png') or file_name.endswith('jpg') or file_name.endswith('jpeg'):
            if os.path.exists(f"{image_folder_path}/image_{i}.{file_name.split('.')[-1]}"):
                continue
            else:
                os.rename(images[i], f"{image_folder_path}/image_{i}.{file_name.split('.')[-1]}")
            continue
        else:
            os.remove(images[i])


def image_resize(image_folder_path, resolution=(1080, 1920)):
    images = [f"{image_folder_path}\\{path}" for path in os.listdir(image_folder_path)]
    for i in images:
        img = Image.open(i)
        if 900 <= img.size[0] >= 1280 and 1880 <= img.size[1] >= 2050:
            image = img.resize(resolution, PIL.Image.ANTIALIAS)
            image.save(i)
        else:
            img.close()
            os.remove(i)


def save_video(image_folder_path, video_folder_path, image_time=4, fps=24):
    images = [f"{image_folder_path}\\{path}" for path in os.listdir(image_folder_path)]
    clips = []
    for i in range(len(images)):
        clip = ImageClip(images[i]).set_duration(image_time)

        clips.append(clip)

    video_clip = concatenate_videoclips(clips, method='compose')

    video_clip.write_videofile(rf"{video_folder_path}/video-output.mp4", fps=fps, remove_temp=True, codec="libx264",
                               audio_codec="aac")


def sub_video(video_folder_path):
    clip = VideoFileClip(rf"{video_folder_path}/video-output.mp4")

    for i in range(0, int(clip.duration), 60):
        videoname = f"{video_folder_path}/video-output_{i}.mp4"
        if not round(clip.duration) - i < 60:
            ffmpeg_extract_subclip(rf"{video_folder_path}/video-output.mp4", i, i + 60, f"{video_folder_path}/video_{i}.mp4")
        else:
            ffmpeg_extract_subclip(rf"{video_folder_path}/video-output.mp4", i, round(clip.duration),
                                   f"{video_folder_path}/video_{i}.mp4")


path = json.load(open('config.json', 'r'))["Image Folder Path"]
video_path = json.load(open('config.json', 'r'))["Video Folder Path"]
filter_image(path)
image_resize(path)
save_video(path, video_path)
sub_video(video_path)

