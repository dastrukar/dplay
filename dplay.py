import os
cmd = ""

# -Functions-

# forms a command to execute with
def gamecommand():
    # load some text files and start some variables
    load = open("dplay.cfg", "r").readlines()
    files = []
    global cmd

    files = getSentences(load)

    # form a command to execute
    for i in files:
        cmd += " "
        cmd += i


# what source port do you want to use???
def getSentences(lst):
    temp = []
    global cmd
    
    for i in lst:
        sentence = i
        # ignore the sentence if it has a '#' at the start of it
        # else append it to the list
        if len(sentence) > 0:
            # define source port
            if sentence[0] == "+" and cmd == "":
                cmd += sentence[1:-1]
            elif sentence[0] != "#" and sentence[0] != "\n":
                temp.append(sentence[:-1])
    
    return temp



# -Main-
gamecommand()
os.system(cmd)
