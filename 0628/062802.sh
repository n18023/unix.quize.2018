#!/bin/bash


if [ "$#" -eq 0 ]; then
	echo Usage: 062802.sh PATH
	exit 1
fi

find $# -type f -name | du -b $# | sort -n | tac | head -n 5
