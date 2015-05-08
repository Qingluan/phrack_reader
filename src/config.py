import sys ,os
import urllib.request as ur 

OS = sys.platform

HOME_DIR = os.environ["HOME"]
LOCAL_DIR = os.path.join(HOME_DIR,".phrack-ezine")



if not  os.path.exists(LOCAL_DIR): 
    os.mkdir(LOCAL_DIR)



# this function for set proxy by -p 'xxx' ,you can extend it to fix all proxy
def proxy_set(argus_str):
    proxy = ur.ProxyHandler({"http":argus_str})
    opener = ur.build_opener(proxy)
    ur.install_opener(opener)


#############  change below options can let progress more
#############   fixable  

# this url must be see all the dir for issues
BASE_URL = "http://www.phrack.org/archives/issues/"


# this templates include all cmmand for program
cmd_templates = {
            'index':'tree ' +LOCAL_DIR,  # this cmd for tree all content in LOC DIR
            "search":"grep -nr \"%s\" "+LOCAL_DIR, # this cmd for search in loc
        }

#this template for match 'issues dir' , 'issus content name','date' by regex
reg_templates = {
            'get_dir':r'(\d+?)/',
            'get_content_name':r'(\d+?\.txt)',
            'get_date':r'(\d{1,2}\-\w{3}\-\d{4}\s\d{2}\:\d{2})\s',
        }
