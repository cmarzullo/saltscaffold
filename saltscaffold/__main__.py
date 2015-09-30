"""Creates a salt formula skeleton of directories"""

import argparse
#from saltscaffold import formulafolders, formulafiles
from saltscaffold import formulafolders
import os

parser = argparse.ArgumentParser(description='Scaffolding tool for salt formulas')
parser.add_argument('-p','--project',required=True, nargs=1, help='The name of the formula to create')

args = parser.parse_args()

cur_dir = os.getcwd()

if args.dir != None
    cur_dir = args.dir[0]

def main():
    try:
        formulafolders.create_folders(args.project[0], cur_dir)
        #formulafiles.create_files(args.project[0], cur_dir)
    except IOError as e:
        print(e.strerror)

if __name__ == '__main__':
    main()

