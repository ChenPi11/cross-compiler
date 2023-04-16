from subprocess import *
works=[]
def automake(configure,profiles,host,builddir,prefix,make_profs):
    p=Popen(f'python3 automake.py "{configure}" "{profiles}" "{host}" "{builddir}" "{prefix}" "{make_profs}"',shell=True)
    #p.wait()
    works.append(p)

def make_wait_all():
    for i in works:
        i.wait()
