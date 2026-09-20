#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """
    Retrieve and parse GitHub event data from the given API URL.

    Args:
        url (str): The GitHub API endpoint to fetch events from.

    Returns:
        list: A list of dictionaries, each representing one GitHub event.
    """
    raw_text = requests.get(url).text
    events = json.loads(raw_text)
    return events


def print_events(events, n=5):
    """
    Print the first n events, each as one line in the form 'type :: repo'.

    Args:
        events (list): A list of GitHub event dictionaries.
        n (int): Number of events to print. Defaults to 5.
    """
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """
    Print GHUSER and url, retrieve GitHub events, and print the first n of them.
    """
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()
