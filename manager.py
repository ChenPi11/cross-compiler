#!/bin/env python3
import whiptail,sys
from install import *
from config import *
from make import *

def comp():
    #w=whiptail.Whiptail("编译")
    d=input("configure所在目录:")
    configure=os.path.abspath(os.path.join(d,"configure"))
    print(d)
    Popen([configure,"--help"]).wait()
    profs=input("编译选项:")
    prefix=input("输出路径")
    cur_ccs=get_conf("gnulinux-ccs",[])
    make_profs=input("MAKE选项")
    for i in cur_ccs:
        BUILD=f"/tmp/cc-build-{i}-linux-gnu"
        try:
            os.makedirs(BUILD)
        except:
            pass
        automake(configure,profs,f"{i}-linux-gnu",BUILD,os.path.abspath(os.path.join(prefix,i)),make_profs)
    make_wait_all()

def main():
    w=whiptail.Whiptail("交叉编译管理器")
    res=w.menu("",("安装GNU/Linux交叉编译环境","编译","退出")).decode()
    print(res)
    if(res=="退出"):
        sys.exit(0)
    elif(res=="安装GNU/Linux交叉编译环境"):
        gnu_linux_i()
    elif(res=="编译"):
        comp()

if(__name__=="__main__"):
    exc=None
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        exc=e
    save_conf()
    if(exc):
        raise exc