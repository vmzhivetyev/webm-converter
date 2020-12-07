import ffmpeg
from ffmpeg import Error
import os
from pathlib import Path


ffmpeg_cmd = 'ffmpeg'

# For Windows
if os.name == 'nt':
    ffmpeg_cmd = 'bin/ffmpeg.exe'


def convert_video(in_file, out_file):
    input_vid = ffmpeg.input(in_file)
    output = ffmpeg.output(input_vid, out_file)
    output = ffmpeg.overwrite_output(output)
    output = output.global_args('-loglevel', 'error')
    output.run(cmd=ffmpeg_cmd)


def convert_all(from_dir, to_dir, target_ext):
    in_files = list(Path(from_dir).rglob('*.*'))
    for idx, in_file in enumerate(in_files):
        webm_name_no_ext = os.path.splitext(os.path.basename(in_file))[0]
        out_file = os.path.join(to_dir, webm_name_no_ext + target_ext)

        if os.path.isfile(out_file):
            print(f'Skipped {in_file} ({out_file} already exists)')
            continue

        print(f'"{in_file}" -> "{out_file}" ({idx+1}/{len(in_files)})')
        convert_video(in_file, out_file)


convert_all(from_dir='_src', to_dir='_mp4', target_ext='.mp4')
