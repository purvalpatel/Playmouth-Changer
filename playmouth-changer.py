#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands





print """
                     Plymouth Theme Changer for Debian Based Distros


________________________________________________________________________________

Themes:
_______
"""


usr=os.getenv ('USER')

os.chdir("/usr/share/plymouth/themes")

def devam():
    idx=commands.getoutput("ls")
    print idx

    thm=raw_input("Enter theme name do you want to select: ")
    print " "

    abc=("plymouth-set-default-theme" + " " + thm)
    a=commands.getoutput (abc)
    print a

    b=commands.getoutput ("update-initramfs -u")
    print b
    print "Theme successfully appilied."


if not usr=="root":
    print "Access denied. You must run this script in root."

else:
    devam()    



