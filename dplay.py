import os
srcprt = "./"

# -Functions-

# forms a command to execute with
def gamecommand():
    # load some text files and start some variables
    load = open("dplay.cfg", "r").readlines()
    files = []
    cmd = ""

    files = getSentences(load)

    # form a command to execute
    for i in files:
        cmd += " "
        cmd += i
    
    # return the command for use
    return cmd


# what source port do you want to use???
def getSentences(lst):
    temp = []
    
    for i in lst:
        # ignore the sentence if it has a '#' at the start of it
        # else append it to the list
        if len(sentence) > 0:
            # define source port
            if sentence[0] == "+" and srcprt == "./":
                srcprt += sentence[1:-1]
            elif sentence[0] != "#":
                temp.append(sentence[-1])
    
    return temp



# -Main-
os.system(gamecommand())
