#!/usr/bin/env python

"""
Extract data from dump1090 process and send it back to gcloud storage

Usage:
    plane.py <url> <bucket> <id> <secret>

Options:
    -h, --help            Display this message.
    -v, --verbose         Display verbose output.
"""
from __future__ import (absolute_import, division, print_function,
                                                unicode_literals)

import json
import requests
import boto
import gcs_oauth2_boto_plugin
import os
import shutil
import StringIO
import tempfile
import time
import subprocess

from docopt import docopt

GOOGLE_STORAGE = 'gs'
LOCAL_FILE = 'file'


def configure_boto(client_id, client_secret):
    gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(client_id, client_secret)


def download_data(url):
    r = requests.get(url)
    if r.json():
        return r.text

def upload_data(bucket, data):
    filename = time.strftime("%Y%m%d-%H%M%S.json")

    dst_uri = boto.storage_uri(bucket + '/' + filename, GOOGLE_STORAGE)
    dst_uri.new_key().set_contents_from_string(data)
    print('Successfully created "%s/%s"' % (
              dst_uri.bucket_name, dst_uri.object_name))

def commit_data(data):
    filename = time.strftime("%Y%m%d-%H%M%S.json")
    cmd = 'echo "{data}" | ssh mlhamel@104.198.222.154 "pachctl put-file flights master {filename} -c"'.format(
        data=data,
        filename=filename,
        )
    subprocess.Popen(cmd, shell=True)
    print('Successfully created commit "%s" with "%s"' % (filename, data))

def main():
    opts = docopt(__doc__)
    configure_boto(opts['<id>'], opts['<secret>'])
    data = download_data(opts['<url>'])
    if data:
        commit_data(data)
    else:
        print("No data")



if __name__ == '__main__':
    main()
