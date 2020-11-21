# Note to future self
(For when you actually start the project)

## Goal
To write a script to decide on the score of a judo throw.

## About libraries
- cv2 is could be the way to go to analyse videos
- pytorch for object detection ?

## TODO
- Check if there's a way to train model without downloading all videos (batch?)
    - If yes: JUST DO IT
    - If no:
        - Write web scraper to get links of videos from IJF
        - Download \*snif\* (will probably limit train size)
- VIDEO SEGMENTATION (extracting main objects from video)
- Key frame extraction ? (i.e. getting only clips of when the action happens)

## Notes
- 700 GB ~ 20 000 (full fight) videos