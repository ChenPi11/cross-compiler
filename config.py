import os,sys,json
CWD=os.path.abspath(os.path.join(os.path.abspath(sys.argv[0]),".."))
DATA_DIR=os.path.join(CWD,"data")
CACHE_FILE=os.path.join(DATA_DIR,"cache.json")
if(not os.path.isdir(DATA_DIR)):
    os.makedirs(DATA_DIR)
if(not os.path.isfile(CACHE_FILE)):
    open(CACHE_FILE,"w").close()

configs={}
try:
    #load conf
    f=open(CACHE_FILE,"r")
    configs=json.load(f)
    f.close()
except (FileNotFoundError,json.decoder.JSONDecodeError) as e:
    open(CACHE_FILE,"w").close()
    print("WARNING:",e)

def save_conf():
    f=open(CACHE_FILE,"w")
    json.dump(configs,f)
    f.close()

def set_conf(k,v,save=True):
    configs[k]=v
    if(save):
        save_conf()
def get_conf(k,d=None):
    return configs.get(k,d)


all_linux_archs=["aarch64","alpha","arm","armhf","hppa","hppa64","i686","m68k","mips","mips64","mips64el",
             "mipsel","mipsisa32r6","mipsisa32r6el","mipsisa64r6","mipsisa64r6el","powerpc","powerpc64",
             "powerpc64le","riscv64","s390x","sh4","sparc64","x86_64","x86_64x32"
]