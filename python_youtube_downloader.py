import json
import re
import urllib.request
import requests

from pytube import YouTube

api_key = "AIzaSyB5KUB_bvYN2KZ-Ph7HKd5FfGFyMZodqz4"
link_file = "test_links.csv"

class Helper:
    def __init__(self):
        pass

    def id_from_url(self, url: str):
        return url.rsplit("/", 1)[1]
    
    def title_to_underscore_title(self, title: str):
        title = re.sub('[\W_]+', "_", title)
        return title.lower()

class YoutubeStats:
    def __init__(self, url: str):
        # self.json_url = urllib.request.urlopen(url)
        # self.data = json.loads(self.json_url.read())
        self.json_url = requests.get(url)
        self.data = json.loads(self.json_url.text)
    
    def print_data(self):
        print(self.data)
    
    def get_video_title(self):
        return self.data['items'][0]['snippet']['title']
    
    def get_video_description(self):
        return self.data['items'][0]['snippet']['description']

    def download_video(self, url: str, title: str):
        YouTube(url).streams.first().download(filename="{}.mp4".format(title))

with open(link_file) as f:
    content = f.readlines()

content = list(map(lambda s: s.strip(), content))
content = list(map(lambda s: s.strip(','), content))

helper = Helper()

for youtube_url in content:
    video_id = helper.id_from_url(youtube_url)
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    yt_stats = YoutubeStats(url)
    title = yt_stats.get_video_title()
    title = helper.title_to_underscore_title(title)
    description = yt_stats.get_video_description()

    with open(f"{title}_description.txt","w") as f:
        f.write(description)
    #yt_stats.download_video(youtube_url, title)





