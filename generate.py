#!/usr/bin/env python
import os
os.system("ffmpeg -i input.mp4 -vf subtitles=input.srt:force_style='Fontsize=30' output.mp4")
os.system("ffmpeg -i output.mp4 -r 10 -vf scale=720:-1 output.gif")