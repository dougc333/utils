

import os,sys,argparse

class LargeFiles:
  def __init__(self):
     parser=argparse.ArgumentParser(description="file name with directory path")
     parser.add_argument("large_filename" ,help="enter filename" )
     args=parser.parse_args()
     print("filename is:",args.large_filename) 
     big_file = os.path.join(os.getcwd(), args.large_filename)
     print(os.path.exists(big_file))
     command_string="git filter-branch --tag-name-filter cat --index-filter 'git rm -r --cached --ignore-unmatch {}' --prune-empty -f -- --all".format(args.large_filename)
     print(command_string)
     os.system(command_string)
     
lf = LargeFiles()

