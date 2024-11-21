#!/bin/bash
# get all the allowed methodss
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
