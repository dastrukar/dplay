import os


# -Functions-

# forms a command to execute with
def gamecommand():
    # load some text files and start some variables
    load = open("dplay.cfg", "r").readlines()
    files = []
    cmd = "./gzdoom"

    for i in load:
        sentence = i[:-1]
        
        # ignore the sentence if it has a '#' at the start of it
        # else append it to the list
        if len(sentence) > 0:
            if sentence[0] != "#":
                files.append(sentence)

    # form a command to execute
    for i in files:
        cmd += " "
        cmd += i
    
    # return the command for use
    return cmd


# -Main-
os.system(gamecommand())
