import pandas as pd
from googleapiclient.discovery import build

api_key = "AIzaSyBi1GYFcxWZdDZLRhf5PS_P77ZVr505ZlQ"

youtube = build(
    'youtube',
    'v3',
    developerKey=api_key
)

video_results = []


def get_all_results():
    search_token = True
    i = 0

    while search_token and i < 5:
        search_response = youtube.search().list(
            type='video',
            q='coding',
            part='snippet',
            maxResults=50
        ).execute()

        print("Response...")

        search_token = search_response.get('nextPageToken')
        video_results.extend(search_response['items'])


get_all_results()

video_ids = [item['id']['videoId'] for item in video_results['items']]
channel_titles = [item["snippet"]["channelTitle"]
                  for item in video_results['items']]
video_titles = [item["snippet"]["title"] for item in video_results['items']]
video_ids[:5], channel_titles[:5], video_titles[:5]

stats = youtube.videos().list(
    part='snippet,statistics',
    id=','.join(video_ids)
).execute()

video_like_count = [int(item['statistics'].get('likeCount', 0))
                    for item in stats['items']]
video_view_count = [int(item['statistics']['viewCount'])
                    for item in stats['items']]
video_comment_count = [int(item['statistics']['commentCount'])
                       for item in stats['items']]


# Create a dictionary with the data
data = {
    'Video Title': video_titles,
    'Video Like Count': video_like_count,
    'Video View Count': video_view_count,
    'Video Comment Count': video_comment_count,
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('video_data.csv', index=False)
