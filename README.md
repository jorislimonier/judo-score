# Goal
To write a script to decide on the score of a judo throw.

**Current completion:**
- [X] Web scrape to get to video page
- [x] Bulk download
- [ ] Determine score


# About libraries
- cv2 is could be the way to go to analyse videos
- pytorch for object detection ?

# TODO
- VIDEO SEGMENTATION (extracting main objects from video)
- Key frame extraction ? (i.e. getting only clips of when the action happens)

# Notes
- 700 GB ~ 20 000 (full fight) videos

# Ideas

- **Attention** algorithm
- Steps
    1. Videos
    2. Squelette (CNN)
    3. is_laid_down? Difference in Y's between feet and hands.

- Features
    - Impact velocity
    - Facing the ground? (Head facing)

- Sequence of images to determine score with number of frames laid_down vs not laid_down