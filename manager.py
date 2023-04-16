#!/bin/env python3
import whiptail,sys
from install import *
from config import *

def main():
    w=whiptail.Whiptail("交叉编译管理器")
    res=w.menu("",("安装GNU/Linux交叉编译环境","退出")).decode()
    print(res)
    if(res=="退出"):
        sys.exit(0)
    elif(res=="安装GNU/Linux交叉编译环境"):
        gnu_linux_i()

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