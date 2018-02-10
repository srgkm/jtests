from collections import Counter, defaultdict
import os
import sys
import re


def main():
    """
    (Hello)

    Task: see name.

    Naive implementation:

    - We expect utf-8 encoded text files
    - We expect mono lang text files, in case of multi lang alpha sorting can be weired
    - We expect plain text (no HTML)
    - No optimizations for reading/sorting very large files

    Usage: python3 ./word_stat.py filename
    """
    try:
        _, filename = sys.argv
    except ValueError:
        sys.stderr.write('Error: bad args')
        return
    if not os.path.exists(filename):
        sys.stderr.write('Error: file %s does not exist' % filename)
        return
    with open(filename, mode='rt') as f:
        text = f.read()
        words = re.findall(r'[-\w]+', text.lower())
        words_grouped_by_counter = defaultdict(list)
        for word, counter in Counter(words).items():
            words_grouped_by_counter[counter].append(word)
        for group, words in sorted(words_grouped_by_counter.items(), key=lambda x: x[0], reverse=True):
            for word in sorted(words):
                print('%s: %s' % (word, group))


if __name__ == '__main__':
    main()
