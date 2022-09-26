#!/bin/sh
curl --fail https://ifdo.ca/~seymour/runabc/top.html 2>/dev/null |grep -E 'abcMIDI-(.*)\.zip' |sed -E 's,(.*)abcMIDI-(.*)\.zip(.*),\2,'
