import os, time, json, winsound, shutil, sys
from tkinter import filedialog

if str(shutil.which("ffmpeg")) == "None":
    print("FFmpeg is not installed in your computer. Please download FFmpeg and add it to PATH. If you need a guide on how to install it, you can watch a tutorial like this one: \033]8;;https://youtu.be/IECI72XEox0\033\\https://youtu.be/IECI72XEox0\033]8;;\033\\")
    time.sleep(1)
    input("Press the enter key to exit ")
    sys.exit()

if not os.path.isdir("Videos"):
    os.makedirs("Videos")

input_video_list = filedialog.askopenfilenames()

for input_video in input_video_list:
    output_video = os.path.basename(input_video)
    output_video = ".".join(output_video.split(".")[:-1])

    os.system(f"ffprobe -hide_banner -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")

    with open("temp.json", "r") as openfile:
        video_data = json.load(openfile)

    duration = float(video_data["format"]["duration"])
    width = int(video_data["streams"][0]["width"])
    height = int(video_data["streams"][0]["height"])
    video_bitrate = (65536 / duration) * 0.99

    if width >= height:
        video_res = "-vf scale=-1:1080"
    if width < height:
        video_res = "-vf scale=1080:-1"
    video_fps = 60
    audio_channel = ""
    audio_bitrate = 128

    if duration >= 31:
        video_res = video_res.replace("1080", "720")
        audio_bitrate = 96

    if duration >= 61:
        video_res = video_res.replace("720", "540")
        audio_bitrate = 64

    if duration >= 91:
        video_res = video_res.replace("540", "480")
        video_fps = 30

    if duration >= 121:
        audio_bitrate = 48

    if duration >= 181:
        video_res = video_res.replace("480", "320")
        audio_bitrate = 32

    if duration >= 301:
        video_res = video_res.replace("320", "240")
        audio_bitrate = 24
        audio_channel = "-ac 1 -apply_phase_inv 0"

    if duration >= 421:
        audio_bitrate = 14

    if width >= height:
        if height <= int(video_res.replace("-vf scale=-1:", "")):
            video_res = ""
    if width < height:
        if width <= int(video_res.replace("-vf scale=", "").replace(":-1", "")):
            video_res = ""

    os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -fpsmax {video_fps} {video_res} -c:v libvpx-vp9 -cpu-used 2 -row-mt 1 -b:v {video_bitrate - audio_bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -fpsmax {video_fps} {video_res} -c:v libvpx-vp9 -cpu-used 2 -row-mt 1 -b:v {video_bitrate - audio_bitrate}k -pass 2 -c:a libopus {audio_channel} -b:a {audio_bitrate}k \"Videos/{output_video}.webm\"")
    
    print("")
    if os.path.isfile("temp.json") == True:
        os.remove("temp.json")
    if os.path.isfile("ffmpeg2pass-0.log") == True:
        os.remove("ffmpeg2pass-0.log")

winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
print("Finished transcoding all videos")
time.sleep(1)