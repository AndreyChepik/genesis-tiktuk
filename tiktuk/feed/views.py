from django.shortcuts import render
import requests


def feed_view(request):
    url = "https://tiktok33.p.rapidapi.com/user/feed/dave.xp"
    headers = {
        'x-rapidapi-host': "tiktok33.p.rapidapi.com",
        'x-rapidapi-key': "c1257dc04cmshd888bbb072eb770p1f2b8ajsnbf16d4cd1d66"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return render(request, 'feed.html', {'videos': 'videos'})