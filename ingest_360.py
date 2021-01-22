import os
import json
import datetime
import time
import wget
import _thread

with open('config.json') as f:
	config = json.load(f)

print("Media Directory: %s" % config["media_dir"])
today = datetime.datetime.now()
if not os.path.isdir(config["media_dir"] + "/" + today.strftime("%Y")):
	print("Year directory %s does not exist, creating" % today.strftime("%Y"))
	os.mkdir(config["media_dir"] + "/" + today.strftime("%Y"))
if not os.path.isdir(config["media_dir"] + "/" + today.strftime("%Y") + "/" + today.strftime("%m")):
	print("Month directory %s does not exist, creating" % today.strftime("%m"))
	os.mkdir(config["media_dir"] + "/" + today.strftime("%Y") + "/" + today.strftime("%m"))
if not os.path.isdir(config["media_dir"] + "/" + today.strftime("%Y") + "/" + today.strftime("%m") + "/" + today.strftime("%d")):
	print("Day directory %s does not exist, creating" % today.strftime("%d"))
	os.mkdir(config["media_dir"] + "/" + today.strftime("%Y") + "/" + today.strftime("%m") + "/" + today.strftime("%d"))

wd = config["media_dir"] + "/" + today.strftime("%Y") + "/" + today.strftime("%m") + "/" + today.strftime("%d") + "/"

def getFile(url,filename):
	image = wget.download(url,wd + filename)

for t in range(4):
	now = datetime.datetime.now()
	for c in config["cameras"]:
		if not os.path.isdir(wd + c["name"]):
			print("Camera directory %s does not exist, creating" % c["name"])
			os.mkdir(wd + c["name"])
		print("Ingesting camera %s" % c["name"])
		_thread.start_new_thread(getFile, (c["url"], c["name"] + "/" + c["name"] + "_" + now.isoformat(timespec='seconds') + ".jpg"))
		#image = wget.download(c["url"],wd + filename)
	time.sleep(15)
