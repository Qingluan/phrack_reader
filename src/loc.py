from .config import LOCAL_DIR
from .config import cmd_templates

import os


def build_dir(dir_name):
    dir_path = os.path.join(LOCAL_DIR,dir_name)
    if os.path.exists(dir_path):
        print("builded ")
        return None
    os.mkdir(dir_path)

def check():
    if not os.path.exists(LOCAL_DIR):
        build_dir(LOCAL_DIR)

def write_to(dir_name,file_name,content):
    file_name = file_name.replace(' ','_')
    file_path = os.path.join(LOCAL_DIR,dir_name,file_name)
    with   open(file_path,"w") as fp:
        fp.write(content)
    print ("save {}  [ok]".format(file_name),end="\r")


def read_dir(*dir_name):
    path = os.path.join(LOCAL_DIR,*dir_name)
    if os.path.exists(path):
        return os.listdir(path)

def read_text(*paths):
    path = os.path.join(LOCAL_DIR,*paths)
    try :
        with open(path,"r") as fp:
            return fp.read()
    except FileNotFoundError as e :
        print ("no loc file , you should try '-n' options  ")

def search(key_words):
    cmd = cmd_templates["search"]
    real_cmd = cmd %(key_words)
    print ("search : ",key_words ,end="\n\n")
    print (os.popen(real_cmd).read())

