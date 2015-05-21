#Phrack  Document
>Include Part
 
- read Phrack ezine  in network
- download to loc 
- use with http proxy
- read from loc
 

## Introduction

this soft just for reading and download  phrack ezine in a easily way for hacker

this soft will create a dir in ~/

## Install

>./install 

## Useage 

phrack -h will give you help

    -p : proxy set 
    -n : from network , <code>default from local</code> 
    -u : update to loc , this options just work within “-n”
    -s : search key word 

## example 

### from loc

> there are two options is import ‘-n ‘ , ’-p’ ,’-u’

> phrack -i  # will give issues  index ,default is read from loc 

> phrack -ii 1 # will show the introduction of first issue

> phrack -d 1  # will show first issue’s content 

> phrack -d 1 -r 1.txt  # will read content of  first issue’s 1.txt 

### from network

> phrack -i  -n  # this will read from www.phrack.org, but not synchro to loc
  
> phrack -i  -nu # will download content to loc 

> phrack -i -nu  -p “x.x.x.x:8888” # this will use http proxy to  execute , this technology will help you out of some rid .


