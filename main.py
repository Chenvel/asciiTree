import time

import os
from rich import print

filenames = ["frame1.txt", "frame2.txt", "frame3.txt", "frame4.txt"]
os.system('clear')


def animate_tree(files):
    frame_counter = 0
    frames = []
    is_count_down = False
    for name in files:
        with open(name, "r") as f:
            frames.append(f.readlines())
    while True:
        frame = frames[frame_counter]

        print("".join(frame))
        if frame_counter == 3:
            is_count_down = True

        if frame_counter == 0:
            is_count_down = False

        if is_count_down:
            frame_counter -= 1
        else:
            frame_counter += 1

        time.sleep(1)
        os.system('clear')


animate_tree(filenames)
