#!/usr/bin/env python
import os
os.system('ffmpeg -i input.srt input.ass')
os.system('ffmpeg -i input.mp4 -vf ass=input.ass output.mp4')
os.system('ffmpeg -i output.mp4 -r 10 -vf scale=480:-1 output.gif')