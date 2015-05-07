import sys ,os
import urllib.request as ur 

OS = sys.platform

HOME_DIR = os.environ["HOME"]

BASE_URL = "http://www.phrack.org/archives/issues/"

LOCAL_DIR = os.path.join(HOME_DIR,".phrack-ezine")

INDEX_FILE = os.path.join(LOCAL_DIR,"INDEX.in")


if not  os.path.exists(LOCAL_DIR): 
    os.mkdir(LOCAL_DIR)


def proxy_set(argus_str):
    proxy = ur.ProxyHandler({"http":argus_str})
    opener = ur.build_opener(proxy)
    ur.install_opener(opener)
