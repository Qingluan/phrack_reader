#!/usr/bin/env python3

import  argparse
from phrack import get_index
from phrack import get_content_dir
from phrack import get_text
from phrack import phrack_paraser

from phrack import proxy_set
from phrack import check
from phrack import search

def parser():
    desc ="""
    """
    parser = argparse.ArgumentParser(usage="this is for read and get phrack ezine",description=desc)
    parser.add_argument('-i','--index',action="store_true",default=False)
    parser.add_argument('-r','--read',default=None)
    parser.add_argument('-u','--upgrade',action="store_true",default=False)
    parser.add_argument('-n','--network',action="store_false",default=True)
    parser.add_argument('-ii','--introduction-issus',default=None)
    parser.add_argument('-d','--dirs',default=None)
    parser.add_argument('-p','--proxy',default=None)

    parser.add_argument('-s','--search',default=None)

    args = parser.parse_args()
    return args



if __name__ == "__main__":
    # check root directory weather exist
    check()

    args = parser()
    if args.proxy:

        # now only support http proxy
        proxy_set(args.proxy)

    if args.index :

        print(get_index(args.network,args.upgrade))
    
    elif args.introduction_issus:
        print (get_text(args.introduction_issus,"1.txt",loc=args.network,update=args.upgrade))

    elif args.read:
        print(get_text(args.dirs,args.read,loc=args.network,update=args.upgrade))


    elif args.dirs:

        print (get_content_dir(args.dirs,loc=args.network,update=args.upgrade))

    elif args.search:
        search(args.search.strip())
