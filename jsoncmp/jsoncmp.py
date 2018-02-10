import json
import sys


def _sorted_json(file_path):
    with open(file_path) as f:
        _s = json.load(f)
        # Sort keys and nested objects
        return json.dumps(_s, sort_keys=True)


def main():
    """
    (Hello)

    Task: cli script for comparing 2 JSON files.

    Some comments:

    - We expect 2 JSON docs as input
    - We don't diff documents, just return equal or not
    - We don't handle possible errors, eg: file not found, file with no JSON and etc

    Usage: python3 ./jsoncmp.py a.json b.json
    """
    _, file_path_a, file_path_b = sys.argv
    if _sorted_json(file_path_a) == _sorted_json(file_path_b):
        print('Identical JSON docs')
    else:
        print('Different JSON docs')


if __name__ == '__main__':
    main()
