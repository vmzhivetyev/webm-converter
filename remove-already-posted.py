import os
from pathlib import Path

from_dir = '_posted'
to_dir = '_mp4'

in_files = list(Path(from_dir).rglob('*.*'))
for idx, in_file in enumerate(in_files):
    webm_name_no_ext = os.path.splitext(os.path.basename(in_file))[0]
    out_file = os.path.join(to_dir, webm_name_no_ext + '.mp4')

    if os.path.isfile(out_file):
        print(f'Removing {out_file}')
        os.remove(out_file)
