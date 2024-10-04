#!/bin/sh
url=$1
curl -sI "$url" | grep "Location:" | cut -d ' ' -f2
