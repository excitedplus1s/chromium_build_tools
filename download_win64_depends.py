#!/usr/bin/env python3
import gclient
import os
import sys
try:
  import urllib2 as urllib
except ImportError:  # For Py3 compatibility
  import urllib.request as urllib
import zipfile
import tarfile

INFRA_URL='https://chrome-infra-packages.appspot.com/'
STORAGE_API_URL = 'https://storage.googleapis.com/'
def get_download_url(originurl):
  remove_platform_url = originurl.replace('${platform}','windows-amd64')
  try:
    import urlparse
  except ImportError:  # For Py3 compatibility
    import urllib.parse as urlparse
  url_path = urlparse.urlparse(remove_platform_url).path.replace('@','/+/',1)
  download_page_url = INFRA_URL + 'p' + url_path
  htmlstr = urllib.urlopen(download_page_url).read().decode()
  start = htmlstr.find(STORAGE_API_URL)
  end = htmlstr.find('"',start)
  import html
  return html.unescape(htmlstr[start:end])

def download_progress(block_num, block_size, total_size):
  display_chars = ['\\','|','/','_']
  sys.stdout.write('\rDownloading, Please wait %s' % (display_chars[block_num % 4]))
  sys.stdout.flush()

if __name__ == '__main__':
  SKIP_PATH_PREFIX='src/'
  options, _ = gclient.OptionParser().parse_args([])
  obj = gclient.GClient.LoadCurrentConfig(options)
  obj.GetCipdRoot()
  sol = obj.dependencies[0]
  sol.ParseDepsFile()
  import shutil
  shutil.rmtree(path=SKIP_PATH_PREFIX, ignore_errors=True)
  for depend in sol.dependencies:
    if depend.should_process and depend.condition:
      install_path = depend.name.split(':')[0][len(SKIP_PATH_PREFIX):]
      print("\rinstall_path: " + install_path)
      installed_path = SKIP_PATH_PREFIX + install_path
      os.makedirs(installed_path)
      if depend.url.startswith(INFRA_URL):
        download_url = get_download_url(depend.url)
        print("download url:" + download_url)
        zip_file , _ = urllib.urlretrieve(download_url, installed_path + '/data.zip', download_progress)
        with zipfile.ZipFile(zip_file, 'r') as zip:
          zip.extractall(installed_path)
        os.remove(zip_file)
      else:
        download_url = depend.url.replace('@','/+archive/',1) + '.tar.gz'
        print("download url:" + download_url)
        targz_file , _ = urllib.urlretrieve(download_url, installed_path + '/data.tar.gz', download_progress)
        with tarfile.open(targz_file) as targz:
          targz.extractall(installed_path)
        os.remove(targz_file)