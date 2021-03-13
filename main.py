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


def convert_takumi(from_dir='E:/Movies/Initial D 4th Stage [RG Genshiken]',
                   to_dir='E:/Movies/Initial D 4th Stage [RG Genshiken]/rus/',
                   target_ext='.mp4'):
    in_files = list(Path(from_dir).glob('*.mkv'))
    for idx, in_file in enumerate(in_files):
        webm_name_no_ext = os.path.splitext(os.path.basename(in_file))[0]
        out_file = os.path.join(to_dir, webm_name_no_ext + target_ext)

        if os.path.isfile(out_file):
            print(f'Skipped {in_file} ({out_file} already exists)')
            continue

        print(f'"{in_file}" -> "{out_file}" ({idx+1}/{len(in_files)})')

        # [RG Genshiken] Initial D 4th Stage - 01 [DVDRip 720x400 x264 AAC].mkv
        # [RG Genshiken] Initial D 4th Stage - 01 [DVDRip 720x400 x264 AAC].[6ch ac3 rus, GitS].mka

        aud_file = 'E:/Movies/Initial D 4th Stage [RG Genshiken]/Rus Audio 5.1/' + os.path.basename(in_file)\
            .replace('.mkv', '.[6ch ac3 rus, GitS].mka')

        input_vid = ffmpeg.input(in_file).video
        input_aud = ffmpeg.input(aud_file).audio
        output = ffmpeg.output(input_vid, input_aud, out_file)
        output = ffmpeg.overwrite_output(output)
        output = output.global_args('-loglevel', 'error')
        output.run(cmd=ffmpeg_cmd)


def merge_movie_and_sound(video_file, audio_file):
    webm_name_no_ext = os.path.splitext(os.path.basename(video_file))[0]
    out_file = os.path.join(os.path.dirname(video_file), webm_name_no_ext + '-good-sound.mkv')

    if os.path.isfile(out_file):
        print(f'Skipped {video_file} ({out_file} already exists)')
        return

    print(f'"{video_file}" -> "{out_file}"')

    input_vid = ffmpeg.input(video_file).video
    input_aud = ffmpeg.input(audio_file).audio
    output = ffmpeg.output(input_vid, input_aud, out_file, codec="copy")
    output = ffmpeg.overwrite_output(output)
    output = output.global_args('-c', 'copy')
    output.run(cmd=ffmpeg_cmd)


# convert_all(from_dir='_src', to_dir='_mp4', target_ext='.mp4')

# convert_takumi()

merge_movie_and_sound(video_file='E:\Movies\Soul.2k.mkv', audio_file='E:\Movies\Soul.rezka.avi')