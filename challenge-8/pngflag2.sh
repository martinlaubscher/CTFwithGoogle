#!/bin/bash

#run from directory where hideandseek.png is located
strings hideandseek.png | grep -Po 'DIH\K(.)' | tr -d '\n' | base64 -d
echo -e
