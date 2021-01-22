# panobot
Auto-ingest 360 camera views, stitch timelapses.

##First step: get images
config.json sets your storage endpoint for image files and the names and urls of the cameras. each camera needs a snapshot endpoint to get a .jpg image file.
run this script as a cron job every minute, and the ingest_360.py will download from all cameras in 15 second increments.

Dependencies:
*Python3
*wget python library:
    pip3 install wget

Directory tree is automatically created in format:
  {your endpoint}/year/month/day/{dir for each camera using name definedin config.json}


crontab example:
  * * * * * cd /panobot && /usr/bin/python3 /panobot/ingest_360.py

where /panobot is the location of this repository, and assuming python3 is in /usr/bin/
