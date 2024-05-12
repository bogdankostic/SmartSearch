#!/usr/bin/env python3
import argparse
import os

from matchers import BaseMatcher

from matchers.boyer_moore import BoyerMooreMatcher
from matchers.naive import NaiveMatcher


DESCRIPTION = """Searches for one or more search patterns in a raw text 
input, text file or a directory consisting of .txt-files and outputs 
all positions the search patterns occur at. 
The default string matching algorithm that is used is the 
Boyer-Moore algorithm. The Naïve string matching algorithm can be used 
by setting the option '-n'. 
"""
NAIVE_HELP = "Use the naive string matching algorithm instead of the Boyer-Moore algorithm."
CASE_HELP = "Perform case-insensitive search."
PATTERNS_HELP = "Search pattern to search for in the provided text inputs."
TEXT_HELP = "Raw text, text file or directory containing txt-files."

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("-n", "--naive", action="store_true", help=NAIVE_HELP)
parser.add_argument("-i", "--case-insensitive", action="store_true", help=CASE_HELP)
parser.add_argument("search_patterns", metavar="SEARCH_PATTERN", nargs="+",  help=PATTERNS_HELP)
parser.add_argument("text", metavar="TEXT_INPUT", help=TEXT_HELP)


def process_directory(directory: str, search_patterns: list[str], matcher: BaseMatcher):
    # iterate over files ending with .txt and search for search patterns
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(f"{directory}/{filename}", "r") as file:
                file_str = file.read()
                for pattern in search_patterns:
                    shifts = matcher.search(pattern, file_str)
                    for shift in shifts:
                        print(f"{filename}\t{pattern}\t{shift}")


def process_file(file: str, search_patterns: list[str], matcher: BaseMatcher):
    with open(file, "r") as file:
        file_str = file.read()
        for pattern in search_patterns:
            shifts = matcher.search(pattern, file_str)
            for shift in shifts:
                print(f"{pattern}\t{shift}")


def process_text(text: str, search_patterns: list[str], matcher: BaseMatcher):
    for pattern in search_patterns:
        shifts = matcher.search(pattern, text)
        for shift in shifts:
            print(f"{pattern}\t{shift}")


def main():
    args = parser.parse_args()
    case_sensitive = not args.case_insensitive
    if args.naive:
        matcher = NaiveMatcher(case_sensitive=case_sensitive)
    else:
        matcher = BoyerMooreMatcher(case_sensitive=case_sensitive)

    # text input is a directory
    if os.path.isdir(args.text):
        process_directory(args.text, args.search_patterns, matcher)

    # text input is a file
    elif os.path.isfile(args.text):
        process_file(args.text, args.search_patterns, matcher)

    # text input is a raw text
    else:
        process_text(args.text, args.search_patterns, matcher)


if __name__ == "__main__":
    main()
