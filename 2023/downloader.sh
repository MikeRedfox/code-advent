#!/bin/bash

TOKEN=53616c7465645f5fe28c2d820def6eb8b15f58857e5af92f38bedf40019c2edc59152f8f2807b6b3ae3bdebbcc7ab1659b1aa766be564116e252f10285222909
YEAR=$2
DAY=$1
URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"
FILE="./input/${DAY}.txt"

curl "${URL}" -H "cookie: session=${TOKEN}" -o "${FILE}" 2>/dev/null
