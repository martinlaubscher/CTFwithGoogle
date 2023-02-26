#!/bin/bash

#run from directory where hideandseek.png is located
xxd -p hideandseek.png | tr -d '\n' | grep -Po '65444948\K(..)' | tr '\n' ' ' | xxd -r -p | base64 -d
echo -e
