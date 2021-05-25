## Goal
To write a script to decide on the score of a judo throw.

**Current completion:**
- [X] Web scrape to get to video page
- [x] Bulk download
- [ ] Determine score

## TODO

### Joris
- Refactor web scraper
- Fix web scraper
    - Use ["judoka" page](https://www.ijf.org/judoka) rather than "ranking"
    - Identify ippon by Hansoku-Make rather than throw
- Characteristics
    - Judoka
        - Number of ippons (with timestamps)
        - Number of waza (with timestamps)
        - Weight category
        - Age
        - ...etc
    - Fight
        - is_ippon
        - number waza
        - correct fights with 2 ippons

- See if metadata can be used to store athlete name (mkv)

### Yann
- [Judo background](https://www.youtube.com/watch?v=pgfKasoI5yc&ab_channel=Judo)
- Papers
    - Share Zotero
    - [Deep skeleton 1](https://arxiv.org/pdf/1609.03659.pdf)
        - Proof of concept on sample video
    - ~~[Deep skeleton 2](https://openaccess.thecvf.com/content_ICCV_2017/papers/Lee_Ensemble_Deep_Learning_ICCV_2017_paper.pdf)~~
- [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf)
- [DVC](https://dvc.org/)

## Ideas

- "**Attention**" algorithm
- Steps
    1. Videos
    2. Squelette (CNN)
    3. is_laid_down? Difference in Y's between feet and hands.
    4. is_score ?

- Features
    - Impact velocity
    - Facing the ground? (Head facing)

- Sequence of images to determine score with number of frames laid_down vs not laid_down

### Data management

- Remove folder organization per athlete (all videos in one folder)
- Video title
    - Keep original title for now
    - Use hash (ID) to identify video
    - Parse (=extract info from video title)


# 1. Videos
# 2. Squelette (CNN)
# 3. is_laid_down? Difference in Y's between feet and hands.
# 4. is_score ?

### References
https://research.fb.com/downloads/detectron/
