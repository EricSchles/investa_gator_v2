from subprocess import call
from multiprocessing import Process
import argparse

def install(requirement,how_to_install,args):
    if args["left_split"]:
        requirement = requirement.split(args["left_split"])[0]
    elif args["right_split"]:
        requirement = requirement.split(args["right_split"])[1]
    if 'sudo' in how_to_install:
        how_to_install = how_to_install.replace("[PACKAGE]",requirement).split(" ")
    else:
        how_to_install = ["sudo"] + how_to_install.replace("[PACKAGE]",requirement).split(" ")
    call(how_to_install)

args = argparse.ArgumentParser()
args.add_argument("-ls","--left-split",help="the package name is to the left of the character or characters to split on")
args.add_argument("-rs","--right-split",help="the package name is to the right of the character or characters to split on")

args = vars(args.parse_args())

with open("requirements.txt","r") as f:
    dependencies = f.read().split("\n")
    dependencies = [dep for dep in dependencies if dep != '']
with open("how_to_install.txt","r") as f:
    how_to_install = f.read().strip()

for dep in dependencies:
    p = Process(target=install,args=(dep,how_to_install,args,))
    p.run()
