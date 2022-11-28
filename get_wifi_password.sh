#!/bin/bash

echo "wifi name:$1"

security find-generic-password -wa $1

