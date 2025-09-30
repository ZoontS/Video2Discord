# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os, time, json, shutil, sys, platform
import typer
from tkinter import filedialog, messagebox, Tk
from typing_extensions import Annotated

def get_default_video_params():
    video_res = 1080
    video_fps = 60
    audio_channel = ""
    audio_bitrate = 192
    return video_res, video_fps, audio_channel, audio_bitrate

def get_webm_params(video_bitrate: float):
    video_res, video_fps, audio_channel, audio_bitrate = get_default_video_params()

    if video_bitrate > 6000:
        video_bitrate = 6000
        audio_bitrate = 128

    if video_bitrate < 4000:
        video_res = 720
        audio_bitrate = 96

    if video_bitrate < 2500:
        video_res = 540
        audio_bitrate = 64

    if video_bitrate < 1500:
        video_res = 480

    if video_bitrate < 600:
        video_res = 360
        video_fps = 30
        audio_bitrate = 48

    if video_bitrate < 276:
        video_res = 240
        audio_bitrate = 24
        audio_channel = "-ac 1 -apply_phase_inv 0"

    if video_bitrate < 150:
        video_res = 144
        audio_bitrate = 14
        
    return video_bitrate, video_res, video_fps, audio_bitrate, audio_channel

def get_mp4_params(video_bitrate: float):
    video_res, video_fps, audio_channel, audio_bitrate = get_default_video_params()

    if video_bitrate > 10000:
        video_bitrate = 10000
        audio_bitrate = 160

    if video_bitrate < 5000:
        video_res = 720
        audio_bitrate = 128

    if video_bitrate < 3000:
        video_res = 540
        audio_bitrate = 96

    if video_bitrate < 2000:
        video_res = 480
        audio_bitrate = 64

    if video_bitrate < 800:
        video_res = 360
        video_fps = 30

    if video_bitrate < 500:
        video_res = 240
        audio_bitrate = 32
        audio_channel = "-ac 1"

    if video_bitrate < 250:
        video_res = 144
        audio_channel = "-ac 1 -ar 16k"
        audio_bitrate = 16
        
    return video_bitrate, video_res, video_fps, audio_bitrate, audio_channel

def main(
    video_file_paths: Annotated[list[str], typer.Argument()] = [],
    video_format: Annotated[str, typer.Option("--format", help="Output video format. Webm has better compression but is slower and less compatible than mp4. Possible values: [webm, mp4]")] = "mp4",
    speed: Annotated[str, typer.Option(help="Compression speed. Slower = better compression quality. Possible values: [fast, medium, slow]")] = "medium",
    size: Annotated[float, typer.Option(help="Target video file size in MB")] = 10,
):
    FILE_SIZE_LIMIT = size # MiB
    ffmpeg = "ffmpeg"
    ffprobe = "ffprobe"

    if video_format not in ("mp4", "webm"):
        raise ValueError("Specified video format not supported")
    if speed not in ("fast", "medium", "slow"):
        raise ValueError("Specified encoding speed not supported")

    if platform.system() == "Windows":
        if os.path.isfile("FFmpeg/bin/ffmpeg.exe") == True and os.path.isfile("FFmpeg/bin/ffprobe.exe") == True:
            print("Using bundled FFmpeg")
            ffmpeg = "FFmpeg\\bin\\ffmpeg.exe"
            ffprobe = "FFmpeg\\bin\\ffprobe.exe"

        if (str(shutil.which("ffmpeg")) == "None" and os.path.isfile("FFmpeg/bin/ffmpeg.exe") == False) or (str(shutil.which("ffprobe")) == "None" and os.path.isfile("FFmpeg/bin/ffprobe.exe") == False):
            print("FFmpeg is not installed in your computer. Please download FFmpeg and add it to PATH. If you need a guide on how to install it, you can watch a tutorial like this one: https://youtu.be/IECI72XEox0")
            input("Press the enter key to exit ")
            sys.exit()
    if platform.system() == "Linux":
        if str(shutil.which("ffmpeg")) == "None" or str(shutil.which("ffprobe")) == "None":
            print("FFmpeg is not installed in your computer. Please install FFmpeg and try again. Example for Debian/Ubuntu: sudo apt install ffmpeg")
            input("Press the enter key to exit ")
            sys.exit()
    if not os.path.isdir("Videos"):
        os.makedirs("Videos")

    if not video_file_paths:
        if platform.system() == "Windows":
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, "Select videos to compress", "Video2Discord", 0) # type: ignore
        elif platform.system() == "Linux":
            root = Tk()
            root.withdraw()
            messagebox.showinfo("Video2Discord", "Select videos to compress", icon="question")
        video_file_paths = filedialog.askopenfilenames() # type: ignore

    for input_video in video_file_paths:
        print(f"Processing {os.path.basename(input_video)}...")
        output_video = os.path.basename(input_video)
        output_video = ".".join(output_video.split(".")[:-1])

        if os.path.isfile(f"Videos/{output_video}.{video_format}") == True:
            suffix = 1
            while os.path.isfile(f"Videos/{output_video} ({suffix}).{video_format}") == True:
                suffix += 1
            output_video = f"{output_video} ({suffix})"

        os.system(f"{ffprobe} -loglevel warning -hide_banner -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")

        with open("temp.json", "r", encoding="utf-8") as openfile:
            video_data = json.load(openfile)

        duration = float(video_data["format"]["duration"])
        width = int(video_data["streams"][0]["width"])
        height = int(video_data["streams"][0]["height"])

        total_kb = FILE_SIZE_LIMIT * 1024 * 8
        video_bitrate = (total_kb / duration)
        if video_bitrate >= 333:
            video_bitrate = video_bitrate * 0.97
        if video_bitrate < 333:
            video_bitrate = video_bitrate - 10

        video_res_arg = ""
        if width >= height:
            video_res_arg = "-vf scale=-2:1080"
        if width < height:
            video_res_arg = "-vf scale=1080:-2"

        if video_format == "webm":
            speed_mappings = {"fast": "5", "medium": "4", "slow": "2"}
            speed = speed_mappings[speed]
            video_bitrate, video_res, video_fps, audio_bitrate, audio_channel = get_webm_params(video_bitrate=video_bitrate)
        elif video_format == "mp4":
            speed_mappings = {"fast": "veryfast", "medium": "fast", "slow": "slow"}
            speed = speed_mappings[speed]
            video_bitrate, video_res, video_fps, audio_bitrate, audio_channel = get_mp4_params(video_bitrate=video_bitrate)
        
        video_res_arg = video_res_arg.replace("1080", str(video_res))

        # Disable video scaling if target resolution is bigger than source resolution
        if width >= height:
            if height <= int(video_res_arg.replace("-vf scale=-2:", "")):
                video_res_arg = ""
        if width < height:
            if width <= int(video_res_arg.replace("-vf scale=", "").replace(":-2", "")):
                video_res_arg = ""

        ffmpeg_args = ""
        pass2_args = ""
        if video_format == "webm":
            ffmpeg_args = f"{ffmpeg} -hide_banner -i \"{input_video}\" -fpsmax {video_fps} {video_res_arg} -sws_flags lanczos+accurate_rnd -c:v libvpx-vp9 -pix_fmt yuv420p -g {video_fps * 5} -keyint_min {video_fps * 3} -lag-in-frames 25 -auto-alt-ref 1 -arnr-maxframes 7 -arnr-strength 4 -enable-tpl 1 -deadline good -cpu-used {speed} -row-mt 1 -b:v {video_bitrate - audio_bitrate}k"
            pass2_args = f"-c:a libopus {audio_channel} -b:a {audio_bitrate}k"
        elif video_format == "mp4":
            ffmpeg_args = f"{ffmpeg} -hide_banner -i \"{input_video}\" -fpsmax {video_fps} {video_res_arg} -sws_flags lanczos+accurate_rnd -c:v libx264 -pix_fmt yuv420p -preset:v {speed} -b:v {video_bitrate - audio_bitrate}k"
            pass2_args = f"-c:a aac {audio_channel} -b:a {audio_bitrate}k -movflags +faststart"
        
        if platform.system() == "Windows":
            print(f"Compressing and saving video to {os.path.abspath(f"Videos/{output_video}.{video_format}")}. Please wait...")
            os.system(f"{ffmpeg_args} -loglevel error -pass 1 -an -y -f null NUL && ^{ffmpeg_args} -loglevel warning -stats -pass 2 {pass2_args} \"Videos/{output_video}.{video_format}\"")
        elif platform.system() == "Linux":
            print(f"Compressing and saving video to {os.path.abspath(f"Videos/{output_video}.{video_format}")}. Please wait...")
            os.system(f"{ffmpeg_args} -loglevel error -pass 1 -an -y -f null /dev/null && \\{ffmpeg_args} -loglevel warning -stats -pass 2 {pass2_args} \"Videos/{output_video}.{video_format}\"")

        if os.path.isfile("temp.json") == True:
            os.remove("temp.json")
        if os.path.isfile("ffmpeg2pass-0.log") == True:
            os.remove("ffmpeg2pass-0.log")
        if os.path.isfile("ffmpeg2pass-0.log.mbtree") == True:
            os.remove("ffmpeg2pass-0.log.mbtree")

    if video_file_paths:
        if platform.system() == "Windows":
            import winsound
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS) # type: ignore
        print("Done!")
        time.sleep(1)

if __name__ == "__main__":
    typer.run(main)