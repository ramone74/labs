import os.path, os

mydir = os.path.abspath(os.curdir)
suf = 0;
myfiles = os.listdir(mydir)

for myfile1 in myfiles:
    short_name1 = os.path.splitext(os.path.basename(myfile1))[0]
    for myfile2 in myfiles:
        short_name2 = os.path.splitext(os.path.basename(myfile2))[0]
        if (short_name1 == short_name2) and (myfile1 != myfile2):
            suf = os.path.splitext(myfile1)[1]
if suf != 0:
    for myfile in myfiles:
        if os.path.splitext(myfile)[1] == suf:
            os.remove(mydir + '/' + myfile)
