from .config import BASE_URL
from .config import LOCAL_DIR
from .config import reg_templates
from .config import cmd_templates

import  urllib.request as ur
import re
import os

from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import concurrent


from .loc import build_dir
from .loc import read_text
from .loc import read_dir
from .loc import write_to


def _get(*sufix,prompt=BASE_URL):
    
    res = ur.urlopen("/".join([prompt]+ list(sufix)))
    
    return res


class phrack_paraser (HTMLParser):
    tagTree = {}
    def __init__(self,tag,*args,**kargs):
        super(phrack_paraser,self).__init__(*args,**kargs)
        self.target = tag
        self.sig = False
        self.result = []

    def handle_starttag(self,tag,attrs):
        if tag == self.target:
            self.sig = True
        

    def handle_endtag(self,tag):
        if self.sig :
            self.sig = False

    def handle_data(self,data):
        if self.sig:
            self.result.append(self.func(data))
    
    def feed(self,text,func):
        self.func = func
        super(phrack_paraser,self).feed(text)
        return self.result

def  get_dir(data):
    cp = re.compile(reg_templates['get_dir'])
    res =  cp.findall(data)
    if res : return res[0]

def get_date(data):
    #cp = re.compile(r'(\d{1,2}\-\w{3}\-\d{4}\s\d{2}\:\d{2})\s')
    cp = re.compile(reg_templates['get_date'])
    return cp.findall(data)

def get_content(data):
    cp = re.compile(reg_templates['get_content_name'])
    return cp.findall(data)

def summary(data,date):
    return list(zip(data[4:],date))

def get_index(loc=True,update=False):
    print (loc,update)
    if loc :#and os.path.exists(INDEX_FILE):
#        return get_content_dir("",loc=True,update=False) 
        os.system(cmd_templates['index'])
    else:
 
        data = _get('').read().decode()
        ht = phrack_paraser("a")
        dirs = ht.feed(data,get_dir)
        date = get_date(data)
        lines =  "\n".join(["date : {}\t date : {}".format(line[0],line[1]) for line in summary(dirs,date)])

        if update:

            [build_dir(dir_n) for dir_n in dirs if dir_n ]

        return lines
        
def get_content_dir(dir_name,loc=True,update=False):
    if loc :
        return read_dir(dir_name)
    else:

        res = _get(dir_name).read().decode()

        ht = phrack_paraser("a")
        content_names = ht.feed(res,get_content)
        content_names = [ f[0] for  f in content_names if f]

        ## this is for download texts 
        downloader(dir_name,content_names)
        ## end ##

        return content_names


def get_text(dir_name,file_name,loc=True,update=False):
    if loc :
        return read_text(dir_name,file_name)

    else:
        print ("download == {}/{} ..".format(dir_name,file_name),end="\r")
        res = _get(dir_name,file_name).read().decode()
        print ("download == {}/{} .. [ok]".format(dir_name,file_name),end="\r")
        if update:
            #print("write to {}/{}".format(dir_name,file_name))

            write_to(dir_name,file_name,res)
        else :
            print (res)

#def update(dirs):
#    results = {} 
#    real_dirs = [ i for i in  dirs if i ]
#    with ThreadPoolExecutor(max_workers=len(real_dirs)) as excutor:
#        futures = { executor.submit(get_one_dir,dr):dr for dr in real_dirs  }
#        
#        for res in concurrent.futures.as_completed(futures):
#            name = futures[res]
#            
#            try:
#                results[name] = res.result()
#            except  Exception as e:
#                print ("error : {}".format(e))


def get_one_dir(dir_name):
    pass
    # syn to loca

def downloader(dir_name,files):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(files)) as executor :
        futures = [ executor.submit(get_text,dir_name,f,False,True) for f in files ]
        
        try:
            [f.result() for f in futures]
        except Exception as err:
            print (err)



if __name__ == "__main__":
    data = _get('').read().decode()
    ht= phrack_paraser("a")
    dirs = ht.feed(data,get_dir)
    date = get_date(data)

    for line  in summary(dirs,date) :
        print ("date : {}  \t date : {} ".format( line[0],line[1] ))
