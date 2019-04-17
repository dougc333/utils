#!/bin/bash

 pscp -h  machine.txt -l dc -Av ../Downloads/cuda-repo-ubuntu1804_10.1.105-1_amd64.deb  /home/dc
