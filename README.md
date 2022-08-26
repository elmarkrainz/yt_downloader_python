# Youtube-Downloader mit Python

A simple intro to solve a problem with python. 

## Eine einfache Problemstellung

Problem: Man will ein YT Video auch offline für rein private Zwecke downloaden.

Wenn ich ein Programm brauche und ich finde kein passendes, dann kann ich selbst eines erstellen.

z.B. meinen eigene YT downloader ohne Werbung oder versteckte Funktionen.


## Was braucht man fürs Erstellen eines einfachen Programms

Man braucht nicht viel, eine passenden Programmiersprache z.b. `Python` und einen Editor um ein Programm zu erstellen.

#### Python

[https://www.python.org/downloads/](https://www.python.org/downloads/)

[https://realpython.com/installing-python/](https://realpython.com/installing-python/)


#### Editor

Das wichtigste Tool aller Developer ist der Editor. Der Editor dient zum Bearbeiten von Text, zum Programmieren, um Code zu bearbeiten und zum Lesen und alles was dazugehört.

Die Auswahl ist groß und jeder hat bald einen eigenen Lieblingseditor.
Beliebte Editoren sind z.B.:

* TextEdit
* Atom
* VS Code
* Notepad
* Notepad++


## Wie erstelle ich ein einfaches Programm?

Für einen YT Downloader braucht man zuerst die richtige Programmbibliothek 

Zum Installieren:

	pip install pytube
		

Mit einem passenden Editor wird ein neues Python File erstellt
	
	ytdownloader.py
	
	
Python-Code für YT downloader

	from pytube import YouTube

	url = 'https://www.youtube.com/watch?v=9ZBmn5AzbPE'
	yt_video = YouTube(url)

	yt_video = yt_video.streams.get_highest_resolution()
	yt_video.download()

	print('your video is downloaded successfully')


ausführen mit

	python ytdownloader.py
	
Video im Ordner öffnen, fertig

## Ein paar Updates für einfachere Bedienung

