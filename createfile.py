import os

def checkConf():
    #if the file doesn't exist, then make a new one
    if not os.path.isfile('dplay.cfg'):
        open('dplay.cfg', 'w+').write("# This is a comment.\n" +
        "# Put a '#' at the start of a sentence to indicate a comment.\n" +
        "#\n" +
        "# This file is used for easily adding launch settings (in case if you're lazy)\n" +
        "#\n" +
        "# Ensure that filenames have no spaces inbetween, and doesn't start with '+'.\n" +
        "# If you want spaces inbetween, start with '+', in a filename, use ''.\n" +
        "#\n" +
        "# Files should be loaded first, whereas launch options should be loaded after.\n" +
        "\n" +
        "# Where is your source port located/name?\n" +
        "SRCPRT=gzdoom\n" +
        "\n" +
        "\n" +
        "# Launch options/parameters go here.\n"
        )
        print('Made a brand new file!')
        return open('dplay.cfg', 'r').readlines()
        
    else:
        print('File already exists.')
        return open('dplay.cfg', 'r').readlines()
