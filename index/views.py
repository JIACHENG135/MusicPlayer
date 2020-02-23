from django.shortcuts import render
from .models import *
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from django.http import HttpResponse 
import requests
from django.views import View

def getJsonFromMusicAPI(apiName):
    # URL = 'http://localhost:4000/'
    URL = "https://netease-ljc.herokuapp.com/"
    URL += apiName
    r = requests.get(URL)
    jsonData = r.json()
    return jsonData 

@require_http_methods(['GET'])
def indexView(request,keyword="周杰伦"):
    # search?keywords= 周杰伦
    hotsong_json = getJsonFromMusicAPI("search?keywords="+keyword)
    data = hotsong_json['result']
    print(type(data))
    songs = []
    ct = 5
    cur = 0
    for song in data['songs']:
        src = getSongUrl(song['id'])
        if cur<ct and src:
            newsong = {}
            newsong['src'] = src
            print(song['id'])
            
            albumId = song['album']['id']
            albumImgUrl = getJsonFromMusicAPI("album?id="+str(albumId))['album']['picUrl']
            newsong['artist'] = song['artists'][0]['name']
            newsong['id'] = song['id']
            
            try:
                newsong['lrc'] = getJsonFromMusicAPI("lyric?id="+str(song['id']))['lrc']['lyric']
            except:
                print("lyric is missing")
                newsong['lrc'] = ''
            newsong['pic'] = albumImgUrl
            newsong['title'] = song['name']
            songs.append(newsong)
            cur += 1
    # print(hotsong_json.keys())
    # for song in hotsong_json:
    #     songUrl = getJsonFromMusicAPI("http://localhost:4000/song/url?id="+str(song["id"]))['data'][0]['url']
    #     print(songUrl)
    #     # song['songUrl'] = songUrl
    # hotsong_json

    return JsonResponse(songs,safe=False)

@require_http_methods(['GET'])
def carouselAPI(request):
    print('carouselAPI is called' )
    return JsonResponse(getJsonFromMusicAPI("album/newest"))

@require_http_methods(['GET'])
def searchSong(requests,keyword="周杰伦"):
    print("searchSong is called")
    return JsonResponse(getJsonFromMusicAPI("search?keywords="+keyword))

@require_http_methods(['GET'])
def getAlbumInfo(requests,albumID):
    songs = []
    data = getJsonFromMusicAPI('album?id='+str(albumID))
    originsongs = data['songs']
    albumImgUrl = getJsonFromMusicAPI("album?id="+str(albumID))['album']['picUrl']
    for song in originsongs:
        newsong = {}
        newsong['artist'] = song['ar'][0]['name']
        newsong['id'] = song['id']
        newsong['src'] = getSongUrl(song['id'])
        try:
            newsong['lrc'] = getJsonFromMusicAPI("lyric?id="+str(song['id']))['lrc']['lyric']
        except:
            print("lyric is missing")
            newsong['lrc'] = ''
        newsong['pic'] = albumImgUrl
        newsong['title'] = song['name']
        songs.append(newsong)
    return JsonResponse(songs,safe=False)


def getSongUrl(songID):
    return getJsonFromMusicAPI("song/url?id="+str(songID))['data'][0]['url']


