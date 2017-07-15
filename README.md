Video Folder Renamer
==================

Renames all folders in a given path to the format of `TITLE (RELEASE_YEAR)` - this script assumes that all folders in the path are movies or TV series and that there are no files (only folders).


## Installation
Clone the repository. This code was written for python 2.7, you should also have [pip](https://pip.pypa.io/en/stable/) installed. To install external dependencies:

`pip install -r requirements.txt`


## Running the script

```
$ ./renamer.py --help
usage: renamer.py [-h] [-t {movie,episode}] [-y] [-d] path

positional arguments:
  path                  path to video folder

optional arguments:
  -h, --help            show this help message and exit
  -t {movie,episode}, --type {movie,episode}
                        type of media files in folder
  -y                    assume yes to everything (non-interactive run)
  -d, --dry-run         dry run (print output but change nothing)
```
