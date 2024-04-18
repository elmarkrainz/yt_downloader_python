# Youtube-Downloader mit Python

A simple intro to solve a problem with python. 

## A simple problem

Problem: I want to download a YT video offline for purely private purposes.

If I need a programme and I can't find a suitable one, then I can create one myself.

e.g. my own YT downloader without adverts or hidden functions.


## What do you need to create a simple programme

You don't need much, a suitable programming language e.g. `Python` and an editor to create a programme.

#### Python

[https://www.python.org/downloads/](https://www.python.org/downloads/)

[https://realpython.com/installing-python/](https://realpython.com/installing-python/)


#### Editor

The most important tool for all developers is the editor. The editor is used for editing text, programming, editing code, reading and everything that goes with it.

There is a large selection and everyone soon has their own favourite editor.
Popular editors are, for example:

* TextEdit
* Atom
* VS Code
* Notepad
* Notepad++


## How do I create a simple programme?

For a YT downloader you first need the right programme library 

To install it:

	pip install pytube
		

A new Python file is created with a suitable editor
	
ytdownloader.py
	

Python code for YT downloader

	from pytube import YouTube

	url = 'https://www.youtube.com/watch?v=9ZBmn5AzbPE'
	yt_video = YouTube(url)

	yt_video = yt_video.streams.get_highest_resolution()
	yt_video.download()

	print('your video is downloaded successfully')

execute with

	python ytdownloader.py
	
Open video in folder, done

## A few updates for easier operation

Add an input option for the YT url
	
	url = (input("paste the YT url: "))
	


