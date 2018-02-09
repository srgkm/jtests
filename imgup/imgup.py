import imghdr
import os
import sys

import requests


IMAGES_ENDPOINT = 'http://httpbin.org/post'


def main():
    """
   (Hello)

   Some comments:

   - We send images one by one (synchronously and slowly)
   - We don't handle server errors (retries in case of 50x and etc)
   - No optimizations for large files

   Usage: python3 ./imgup.py images
   """
    _, img_root = sys.argv
    sess = requests.Session()
    for (root, dir_names, file_names) in os.walk(img_root):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            # Check image
            img_ext = imghdr.what(file_path)
            if img_ext is None:
                continue
            # Send image
            with open(file_path, 'rb') as img_f:
                try:
                    resp = sess.post(
                        IMAGES_ENDPOINT,
                        files={'image': (file_name, img_f, 'image/%s' % img_ext)}
                    )
                    if resp.ok:
                        print('UPLOADED: %s' % file_path)
                    else:
                        # Server error
                        print('FAILED: %s' % file_path)
                except requests.RequestException:
                    # Network error
                    print('FAILED: %s' % file_path)


if __name__ == '__main__':
    main()
