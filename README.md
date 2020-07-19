# aimppl4tosmpl
Playlist converter... Convert .Aimppl4 to .Smpl

Samsung Music doesn't support m3u which is universal playlist format. only supports .smpl which is just a JSON file.

I'm using AIMP3 on my desktop and using Samsung Music on my phone(Samsung Galaxy Note 9), and I wanted to export my playlists from PC to Phone so I had to make this converter.

Only supports .aimppl4 to .smpl.
You might need to change the path (hardcoded path: /storage/emulated/0/ ) if you are using different phone from mine.

Import might be difficult due to existing playlists backups. If this happened to you, I recommend you to just rename your converted smpls so that you can easily recognize them and throw it into /SamsungMusic/Playlists.

You must install python 3.8 to use this script.

Usage

python aimppl4smpl.py <orgfilename.aimppl4> <savefilename.smpl>
