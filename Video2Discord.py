import os
import json

def create_config(folder):
    input_folder = input("Input Folder: ")
    output_folder = input("Output Folder: ")
    suffix = input("Filename Suffix: ")
    
    config = {
        "inputFolder": input_folder,
        "outputFolder": output_folder,
        "suffix": suffix
    }

    json_object = json.dumps(config, indent=4)

    with open(f"{folder}\\config.json", "w") as outfile:
        outfile.write(json_object)

script_folder = os.path.dirname(os.path.abspath(__file__))

if os.path.isfile(f"{script_folder}\\config.json") == False:
    create_config(script_folder)

with open(f"{script_folder}\\config.json", "r") as openfile:
    config = json.load(openfile)

os.chdir(config["inputFolder"])
outfolder = config["outputFolder"]
suffix = config["suffix"]

while True:
    input_video = input("\nInsert File Name: ")
    output_video = ".".join(input_video.split(".")[:-1])

    os.system(f"ffprobe -of json -select_streams v -show_format -show_streams -i \"{input_video}\" -o \"temp.json\"")

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
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:1080 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:1080 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{outfolder}{output_video}{suffix}.webm\"")
    
        elif duration < 61:
            bitrate -= 96
            if height >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{outfolder}{output_video}{suffix}.webm\"")
        
        elif duration < 91:
            bitrate -= 64
            if height >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:720 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 121:
            bitrate -= 64
            if height >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:480 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=-1:480 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 181:
            bitrate -= 48
            if height >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:480 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 301:
            bitrate -= 32
            if height >= 320:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:320 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:320 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 421:
            bitrate -= 24
            if height >= 240:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:240 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:240 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{outfolder}{output_video}{suffix}.webm\"")

        else:
            bitrate -= 12
            if height >= 144:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:144 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=-1:144 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{outfolder}{output_video}{suffix}.webm\"")

    else:
        if duration < 31:
            bitrate -= 128
            if width >= 1080:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=1080:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=1080:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 128k \"{outfolder}{output_video}{suffix}.webm\"")
    
        elif duration < 61:
            bitrate -= 96
            if width >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 96k \"{outfolder}{output_video}{suffix}.webm\"")
        
        elif duration < 91:
            bitrate -= 64
            if width >= 720:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=720:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 121:
            bitrate -= 64
            if width >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=480:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -vf scale=480:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 64k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 181:
            bitrate -= 48
            if width >= 480:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=480:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 48k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 301:
            bitrate -= 32
            if width >= 320:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=320:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=320:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 32k \"{outfolder}{output_video}{suffix}.webm\"")

        elif duration < 421:
            bitrate -= 24
            if width >= 240:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=240:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=240:-1 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -b:a 24k \"{outfolder}{output_video}{suffix}.webm\"")

        else:
            bitrate -= 12
            if width >= 144:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=144:-1 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -vf scale=144:-1 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{outfolder}{output_video}{suffix}.webm\"")
            else:
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 1 -an -y -f webm NUL")
                os.system(f"ffmpeg -hide_banner -loglevel warning -stats -i \"{input_video}\" -c:v libvpx-vp9 -pix_fmt yuv420p -cpu-used 3 -row-mt 1 -fpsmax 30 -b:v {bitrate}k -pass 2 -c:a libopus -ac 1 -b:a 12k \"{outfolder}{output_video}{suffix}.webm\"")

    if os.path.isfile("temp.json") == True:
        os.remove("temp.json")
    if os.path.isfile("ffmpeg2pass-0.log") == True:
        os.remove("ffmpeg2pass-0.log")

    flag = input("\nDo you want to transcode another video? (Y/N): ")
    if flag == "y" or flag == "Y":
        continue
    else:
        break