#!/usr/bin/env python
import os
os.system('ffmpeg -i input2.srt input.ass')
os.system('ffmpeg -i input2.mp4 -vf ass=input.ass output2.mp4')
os.system('ffmpeg -i output2.mp4 -r 10 -vf scale=720:-1 output2.gif')