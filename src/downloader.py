import pytube


class Downloader:
    def download_video(url, location=None):
        """download the video at a given url"""
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download(location)
