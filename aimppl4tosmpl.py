# -*- coding: utf-8 -*-
import json
import argparse
import os

parser = argparse.ArgumentParser(description='aimppl4 to smpl')
parser.add_argument('filename',type=str,help='converting target(.aimppl4)')
parser.add_argument('targetname',type=str,help='target file(.smpl)')
args = parser.parse_args()
filename = args.filename
targetname = args.targetname

file = open(filename,encoding="utf_16_le")
class Smpl_data_class:

    def __init__(self,name):
        self.smpl_data = {
        "members":[],
        "name":"",
        "recentlyPlayedDate":1595185475,
        "sortBy":4,
        "version":1
        }
        self.smpl_data["name"]=name
    
    def addTrack(self,track):
        self.smpl_data["members"].append(track)

    def displayMembers(self):
        print(self.smpl_data)

class Track:

    def __init__(self,artist,info,order,title,_type):
        self.track_data = {
            "artist":"",
            "info":"",
            "order":0,
            "title":"",
            "type":0
        }
        self.track_data["artist"]=artist
        self.track_data["info"]=info
        self.track_data["order"]=order
        self.track_data["title"]=title
        self.track_data["type"]=_type

playlistName=""
Tracks = []

trackcount = 0
for line in file.readlines():
    if "Name=" in line:
        playlistName=line.split("=")[1].strip()
    if "|" in line: # 0: info 1: title 2: artist
        linesplit = line.split("|")
        linesplit[0] = linesplit[0].replace("D:\\",'/storage/emulated/0/').replace("\\","/")
        if not linesplit[1]:
            linesplit[1]=os.path.basename(linesplit[0])
            linesplit[1]=os.path.splitext(linesplit[1])[0]
        if not linesplit[2]:
            linesplit[2]="\u003cunknown\u003e"
        temp = Track(linesplit[2],linesplit[0],trackcount,linesplit[1],65537)
        trackcount += 1
        Tracks.append(temp)

target = Smpl_data_class(playlistName)

for track in Tracks:
    target.addTrack(track.track_data)

    
with open(targetname,"w",encoding="UTF-8") as json_file:
    json.dump(target.smpl_data,json_file,sort_keys=True,ensure_ascii=False)
