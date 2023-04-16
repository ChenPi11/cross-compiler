#!/sbin/nologin
# -*- encoding: utf-8 -*-
import os, platform
import whiptail
from config import *
print(configs)
_installed=get_conf("gnulinux-ccs",[])
linux_archs=[]
for i in all_linux_archs:
    if(not i in _installed):
        linux_archs.append(i)

def get_debian_pkgname(arch):
    if(arch==platform.uname().machine):
        return "gcc"
    if(arch=="arm"):
        return "gcc-arm-linux-gnueabi"
    if(arch=="armhf"):
        return "gcc-arm-linux-gnueabihf"
    elif(arch=="mips64"):
        return "gcc-mips64-linux-gnuabi64"
    elif(arch=="mips64el"):
        return "gcc-mips64el-linux-gnuabi64"
    elif(arch=="mipsisa64r6"):
        return "gcc-mipsisa64r6-linux-gnuabi64"
    elif(arch=="mipsisa64r6el"):
        return "gcc-mipsisa64r6el-linux-gnuabi64"
    elif(arch=="x86_64x32"):
        return "gcc-x86-64-linux-gnux32"
    else:
        return f"gcc-{arch}-linux-gnu"

def install_cc(archs):
    l=[]
    for i in archs:
        l.append(get_debian_pkgname(i))
    paks=" ".join(l)
    os.system(f"sudo apt install {paks}")
    set_conf("gnulinux-ccs",get_conf("gnulinux-ccs",[])+archs)

def apt_update():
    os.system("sudo apt update")

def term_size():
    return os.get_terminal_size().lines,os.get_terminal_size().columns

def gnu_linux_i():
    w=whiptail.Whiptail("安装GNU/Linux交叉编译环境","",term_size()[0],term_size()[1]//2)
    if(len(linux_archs)==0):
        w.alert("所有编译环境均已安装")
        return 0
    _=linux_archs+["全部"]
    res=w.menu("安装哪个编译环境？",_).decode()
    l=[]
    if(res==""):
        return
    if(res=="全部"):
       l=linux_archs
    else: 
        l=[res]
    print(l)
    install_cc(l)
