# Note to future self
(For when you actually start the project)

## Goal
To write a script to decide on the score.

## About libraries
- pytube seems to download Youtube videos just fine, even with the weird Youtube from IJF (like [that](https://www.youtube.com/embed/IZwd2xiGoyA?start=17&autoplay=1&enablejsapi=1&origin=https%3A%2F%2Fwww.ijf.org&widgetid=1))
- cv2 is could be the way to go to analyse videos

## TODO
- Check if there's a way to train model without downloading all videos (batch?)
    - If yes: JUST DO IT
    - If no:
        - Write web scraper to get links of videos from IJF
        - Download \*snif\* (will probably limit train size)
- VIDEO SEGMENTATION (extracting main objects from video)
- Key frame extraction ? (i.e. getting only clips of when the action happens)