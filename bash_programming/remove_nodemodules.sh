#https://unix.stackexchange.com/questions/108216/find-with-execdir
#key is to add {}/node_modules which adds the subdirectory name to the 
#node_modules subdirectory one level down
#!/bin/bash

#https://unix.stackexchange.com/questions/108216/find-with-execdir
#this removes all node_module directories from where this program is run
#mkdir -p /a/node_modules
#mkdir -p /b/node_modules
#would  remove node_modules from a and b

find . -maxdepth 1 -type d -execdir rm -rf {}/node_modules \;

