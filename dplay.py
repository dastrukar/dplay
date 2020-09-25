import os
import createfile

# -Functions-
# get the source port
def getSource(lst):
    for i in lst:
        if len(i) > 0:
            # define source port
            if i[0:7] == 'SRCPRT=':
                print("Source Port: " + i[7:-1])
                return i[7:-1]
    return ''


def getSentences(lst):
    # ignore the sentence if it has a '#' at the start of it or is a '\n'
    # else append it to the list
    lst = [ i for i in lst if i[0] != '#' and i[0] != '\n' and i[0:7] != 'SRCPRT=' ]
    
    # get rid of the \n
    for i in lst:
        if i[-1] == '\n':
            lst[lst.index(i)] = i[:-1]
    
    return lst



# -Main-
# load some text files and start some variables
load = createfile.checkConf()
cmd = getSource(load)
files = getSentences(load)

# form a command to execute
for i in files:
    cmd += ' '
    cmd += i
print(cmd)
# execute command
os.system(cmd)
