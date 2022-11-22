import os
import json
from tkinter import filedialog

script_folder = os.path.dirname(os.path.abspath(__file__)) + "\\"
if not os.path.exists(f"{script_folder}Videos"):
    os.makedirs(f"{script_folder}Videos")

while True:
    input_video = filedialog.askopenfilename().replace("/", "\\")
    output_video = os.path.basename(input_video)
    output_video = ".".join(output_video.split(".")[:-1])

    os.system(f"ffprobe -hide_banner -loglevel warning -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")

    with open("temp.json", "r") as openfile:
        video_data = json.load(openfile)

    duration = float(video_data["format"]["duration"])
    width = int(video_data["streams"][0]["width"])
    height = int(video_data["streams"][0]["height"])
    bitrate = 65536 / duration

    if width > height:
        if duration < 31:
            bitrate -= 128
            if height >= 1080:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:1080 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:1080 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Videos\\{output_video}.webm\"")
    
        elif duration < 61:
            bitrate -= 96
            if height >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 91:
            bitrate -= 64
            if height >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:720 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:720 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")
        
        elif duration < 121:
            bitrate -= 64
            if height >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 181:
            bitrate -= 48
            if height >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 301:
            bitrate -= 32
            if height >= 320:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:320 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:320 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 421:
            bitrate -= 24
            if height >= 240:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:240 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:240 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Videos\\{output_video}.webm\"")

        else:
            bitrate -= 12
            if height >= 144:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:144 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:144 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Videos\\{output_video}.webm\"")

    else:
        if duration < 31:
            bitrate -= 128
            if width >= 1080:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=1080:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=1080:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{script_folder}Videos\\{output_video}.webm\"")
    
        elif duration < 61:
            bitrate -= 96
            if width >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{script_folder}Videos\\{output_video}.webm\"")
        
        elif duration < 91:
            bitrate -= 64
            if width >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=720:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=720:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 121:
            bitrate -= 64
            if width >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 181:
            bitrate -= 48
            if width >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 301:
            bitrate -= 32
            if width >= 320:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=320:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=320:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{script_folder}Videos\\{output_video}.webm\"")

        elif duration < 421:
            bitrate -= 24
            if width >= 240:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=240:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=240:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{script_folder}Videos\\{output_video}.webm\"")

        else:
            bitrate -= 12
            if width >= 144:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=144:-1 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=144:-1 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Videos\\{output_video}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f null NUL && ^ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{script_folder}Videos\\{output_video}.webm\"")

    if os.path.isfile("temp.json") == True:
        os.remove("temp.json")
    if os.path.isfile("ffmpeg2pass-0.log") == True:
        os.remove("ffmpeg2pass-0.log")

    flag = input("\nDo you want to transcode another video? (Y/N): ")
    if flag == "y" or flag == "Y":
        continue
    else:
        break