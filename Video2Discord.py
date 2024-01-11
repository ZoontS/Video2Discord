# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os, time, json, winsound, shutil, sys
from tkinter import filedialog

ffmpeg = "ffmpeg"
ffprobe = "ffprobe"

if os.path.isfile("FFmpeg/bin/ffmpeg.exe") == True and os.path.isfile("FFmpeg/bin/ffprobe.exe") == True:
    print("using bundled FFmpeg")
    ffmpeg = "FFmpeg\\bin\\ffmpeg.exe"
    ffprobe = "FFmpeg\\bin\\ffprobe.exe"

if (str(shutil.which("ffmpeg")) == "None" and os.path.isfile("FFmpeg/bin/ffmpeg.exe") == False) or (str(shutil.which("ffprobe")) == "None" and os.path.isfile("FFmpeg/bin/ffprobe.exe") == False):
    print("FFmpeg is not installed in your computer. Please download FFmpeg and add it to PATH. If you need a guide on how to install it, you can watch a tutorial like this one: https://youtu.be/IECI72XEox0")
    time.sleep(1)
    input("Press the enter key to exit ")
    sys.exit()

if not os.path.isdir("Videos"):
    os.makedirs("Videos")

input_video_list = filedialog.askopenfilenames()

for input_video in input_video_list:
    output_video = os.path.basename(input_video)
    output_video = ".".join(output_video.split(".")[:-1])

    if os.path.isfile(f"Videos/{output_video}.webm") == True:
        suffix = 1
        while os.path.isfile(f"Videos/{output_video} ({suffix}).webm") == True:
            suffix += 1
        output_video = f"{output_video} ({suffix})"

    os.system(f"{ffprobe} -hide_banner -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")

    with open("temp.json", "r") as openfile:
        video_data = json.load(openfile)

    duration = float(video_data["format"]["duration"])
    width = int(video_data["streams"][0]["width"])
    height = int(video_data["streams"][0]["height"])
    video_bitrate = (204800 / duration)
    if video_bitrate >= 1000:
        video_bitrate = video_bitrate * 0.99
    if video_bitrate < 1000:
        video_bitrate = video_bitrate * 0.98

    if width >= height:
        video_res = "-vf scale=-1:1080"
    if width < height:
        video_res = "-vf scale=1080:-1"
    video_fps = 60
    audio_channel = ""
    audio_bitrate = 128

    if video_bitrate > 6000:
        video_bitrate = 6000

    if video_bitrate < 3000:
        video_res = video_res.replace("1080", "720")
        audio_bitrate = 96

    if video_bitrate < 1500:
        video_res = video_res.replace("720", "540")
        audio_bitrate = 64

    if video_bitrate < 1000:
        video_fps = 30

    if video_bitrate < 750:
        video_res = video_res.replace("540", "480")

    if video_bitrate < 564:
        audio_bitrate = 48

    if video_bitrate < 448:
        video_res = video_res.replace("480", "360")
        
    if video_bitrate < 348:
        video_res = video_res.replace("360", "240")
        audio_bitrate = 32

    if video_bitrate < 232:
        audio_bitrate = 24
        audio_channel = "-ac 1 -apply_phase_inv 0"

    if video_bitrate < 160:
        video_res = video_res.replace("240", "144")
        audio_bitrate = 14

    if width >= height:
        if height <= int(video_res.replace("-vf scale=-1:", "")):
            video_res = ""
    if width < height:
        if width <= int(video_res.replace("-vf scale=", "").replace(":-1", "")):
            video_res = ""

    os.system(f"{ffmpeg} -hide_banner -loglevel warning -stats -i \"{input_video}\" -fpsmax {video_fps} {video_res} -c:v libvpx-vp9 -cpu-used 2 -row-mt 1 -b:v {video_bitrate - audio_bitrate}k -pass 1 -an -y -f null NUL && ^{ffmpeg} -hide_banner -loglevel warning -stats -i \"{input_video}\" -fpsmax {video_fps} {video_res} -c:v libvpx-vp9 -cpu-used 2 -row-mt 1 -b:v {video_bitrate - audio_bitrate}k -pass 2 -c:a libopus {audio_channel} -b:a {audio_bitrate}k \"Videos/{output_video}.webm\"")
    
    print("")
    if os.path.isfile("temp.json") == True:
        os.remove("temp.json")
    if os.path.isfile("ffmpeg2pass-0.log") == True:
        os.remove("ffmpeg2pass-0.log")

if input_video_list:
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    time.sleep(1)