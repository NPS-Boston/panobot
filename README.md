# panobot
Auto-ingest 360 camera views, stitch timelapses.

## First step: get images
config.json sets your storage endpoint for image files and the names and urls of the cameras. each camera needs a snapshot endpoint to get a .jpg image file.
run this script as a cron job every minute, and the ingest_360.py will download from all cameras in 15 second increments.

Dependencies:
* Python3
* wget python library:
    pip3 install wget

Directory tree is automatically created in format:
  {your endpoint}/year/month/day/{dir for each camera using name definedin config.json}


crontab example:

    * * * * * cd /panobot && /usr/bin/python3 /panobot/ingest_360.py

where /panobot is the location of this repository, and assuming python3 is in /usr/bin/
By default, the ingest script looks for config.json. Optionally, a different config file can be supplied as an argument, i.e.

    python3 ingest_360.py other_conf.json

Config file is fairly straightforward, requiring a directory for the data to be stored in, and then an array of each camera to poll, where each camera gets a name and the url endpoint.
