# _recognizer

This is an under developmet projet of my idea of recognizing people from videos stored in the local storage of computer.

The program will take a video file as input (currently supporting only .mp4 format)

Then it will filter the video based on frame height only videos with 720p or greater will be considered valid.

Then the program take images of every face it recognize and saves 1 copy of each face.(Currently stuck at this point)

The last step is sending the image to google search by image and reciving the data from there and renameing the video after the
recognized person.(Currently having no idea how to do this)

It has two file:
1. frame.py for filtering the videos according to frame height.
2. VideoFrameFilter.py for recognizing and searching the person.
