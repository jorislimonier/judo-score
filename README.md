<!-- Speak with https://github.com/lancew and see if API is available for judobase -->
## Goal
To write a script to decide on the score of a judo throw.

## TODO

### Joris
- Refactor web scraper
- Fix web scraper
    - [x] Use ["judoka" page](https://www.ijf.org/judoka) rather than "ranking"
    - [ ] Identify ippon by Hansoku-Make rather than throw
- Characteristics
    - Judoka
        - [x] Family name
        - [x] Given name
        - [x] Country
        - [ ] Number of ippons
        - [ ] Number of waza
        - [x] Weight category
        - [ ] Age\
        ...etc
    - Fight
        - is_ippon
        - number waza
        - correct fights with 2 ippons
    - Start organising with Pandas, move to databases later.
    - Multi-threading ?

- See if metadata can be used to store athlete name (mkv)

### Yann
- [Judo background](https://www.youtube.com/watch?v=pgfKasoI5yc&ab_channel=Judo)
- [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf)
- [DVC](https://dvc.org/)

## Ideas
- Features
    - Impact velocity
    - Facing the ground? (Head facing)

- Sequence of images to determine score with number of frames laid_down vs not laid_down

# 1. Videos
### Data management
- Remove folder organization per athlete (all videos in one folder)
- Video title
    - Keep original title for now
    - Use hash (ID) to identify video
    - Parse (=extract info from video title)


# 2. Image segmentation (CNN)

## Ideas
### Model Zoo
- Unet* (human shape segmentation)
- [Bodypix](https://blog.tensorflow.org/2019/11/updated-bodypix-2.html)* TensorFlow.js (human segmentation + body part identification)
- DeepSkeleton (multiple CNN kernels for [medial axis](https://www.wikiwand.com/en/Medial_axis) detection)
- Holistically-Nested Edge Detection (powerful edge detector ~oriented gradients)

\*: pre-trained models available!
### Algorithm pipeline
- 1. Segmentation box

- 2. Segmentation silhouette (edge detection)
- [keras_segmentation](https://github.com/divamgupta/image-segmentation-keras)

- 3. Skeletonization
- Apply "[grassfire transform](https://www.wikiwand.com/en/Grassfire_transform)" as **feature extraction** algorithm?
- DeepSkeleton (the source is closed :/)

- 4. Color cue

- "**Attention**" algorithm

### Techniques
- Transfer learning (with fine tuning on our task)
- GPU

# 3. is_laid_down? 
* Difference in Y's between feet and hands.
* 

# 4. Score detection
## I. Score vs not score
## II. Waza-ari vs ippon
