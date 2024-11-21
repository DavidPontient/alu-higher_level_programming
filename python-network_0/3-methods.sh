#!/bin/bash
# get all the allowed methodss
curl -sI -X OPTIONS "$URL" | grep -i "Allow" | cut -d " " -f2-
