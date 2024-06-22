from googleapiclient.discovery import build

api_key = "AIzaSyDIfoF7D2cpoA9FOaZWKtGKsmwm5zMkcj4"

youtube = build(
    'youtube',
    'v3',
    developerKey=api_key
)

request = youtube.channels().list(
    part='statistics',
    forUsername="BBCNews"
)

response = request.execute()
print(response)
