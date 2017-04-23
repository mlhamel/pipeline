import os
import shutil

SRC_DATA_PATH = "/pfs/data"

def move_per_day(dirpath, filename, dstpath="/pfs/out"):
    date, timestamp = filename.split("-")
    src = os.path.join(dirpath, filename)
    dst = os.path.join(dstpath, date)
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.move(src, dst)


def main():
    for dirpath, dirs, files in os.walk(SRC_DATA_PATH):
       for filename in files:
           move_per_day(dirpath, filename)


if __name__ == '__main__':
    main()
