#!/usr/bin/env python

import os
import argparse
import requests
from imdb import IMDb
from guessit import guessit

imdb = IMDb()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to video folder')
    parser.add_argument('-t', '--type', choices=['movie', 'episode'],
                        default='movie', help='type of media files in folder')
    parser.add_argument('-y', action='store_true',
                        help='assume yes to everything (non-interactive run)')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='dry run (print output but change nothing)')
    return parser.parse_args()


def get_dirs(path):
    return (path, os.listdir(path))


def get_imdb_year(title):
    return imdb.search_movie(title)[0]['year']


def construct_name(directory, args):
    guess = guessit(directory, {
        'type': args.type,
        'allowed_countries': 'usa'  # this avoids wrong parsing of names
    })
    if guess.has_key('year'):
        year = guess['year']
    else:
        year = get_imdb_year(guess['title'])
    return '%s (%s)' % (guess['title'], year)


def main():
    args = parse_args()
    answer = None
    if args.dry_run:
        print('This is a dry-run, will not rename anything')
    print('Working on directory %s' % args.path)
    parent, dirs = get_dirs(args.path)
    for d in dirs:
        print('current directory: %s' % os.path.join(parent, d))
        new_name = construct_name(d, args)
        if d == new_name:
            print('Nothing to change, skipping...')
            continue
        if args.dry_run:
            print('renaming %s -> %s' % (d, new_name))
            continue
        if not args.y:
            answer = raw_input(
                'rename \'%s\' to \'%s\'? (y/n) ' % (d, new_name))
        if answer == 'y' or args.y:
            print('renaming %s -> %s' % (d, new_name))
            os.rename(os.path.join(parent, d), os.path.join(parent, new_name))

if __name__ == '__main__':
    main()
