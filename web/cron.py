from pusher import run
import time
from sys import argv
while True:

    msg = argv[1]
    on_heroku = False
    try:
        msg = argv[2]
        on_heroku = True
    except:
        run(first=msg,second=on_heroku)
    run(first=msg,second=on_heroku)
    
    try:
        time.sleep(int(argv[3]))
    except:
        time.sleep(300) #sleep for five minutes
