import time
def run(first="",second=False):
    from subprocess import call

    call(["git","add","-A"])
    call(["git","commit","-a","-m",first])
    call(["git","push"])
    if second:
        call(["git","push","heroku","master"])

if __name__ == '__main__':
    from sys import argv
    msg = argv[1]
    on_heroku = False
    try:
        msg = argv[2]
        on_heroku = True
    except:
        run(first=msg,second=on_heroku)
    run(first=msg,second=on_heroku)
