#!/bin/bash

echo "start test.sh"

if [ -f "../Downloads/cuda-repo-ubuntu1804_10.1.105-1_amd64.deb" ]; then
  echo "cuda 10 repo exists"; 
else
  echo "cuda 10 repo does not exist..download from nvidia site into ../Downloads"
fi
echo "end test.sh"
