#!/usr/bin/env python3
"""Retrieve print world from URL.

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from URL.
    
    Args:
        urls: The URL of a UTF-8 text document.

    Returns: A list of strings containing words 
            from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(story_words):
    for item in story_words:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1]) # The 0th argument is the module filename 
