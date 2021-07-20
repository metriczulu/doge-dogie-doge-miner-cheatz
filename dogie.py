from pynput import keyboard as kb
from time import sleep

current = set()
tracking = False

def on_press(key):
    if key in {kb.Key.space, kb.Key.shift, kb.Key.esc}:
        current.add(key)


def on_release(key):
    global current
    try:
        current.remove(key)
    except KeyError:
        pass

controller = kb.Controller()
listener = kb.Listener(on_press=on_press, on_release=on_release)

def tap(keys, time=0, controller=controller):
    for key in keys:
        controller.press(key=key)
    sleep(time)
    for key in keys:
        controller.release(key=key)


if __name__ == "__main__":
    print("*** STARTING HACKZORRZZ ***")
    listener.start()

    while True:
        if current == {kb.Key.shift, kb.Key.space}:
            tracking = not tracking
            print(f"Hackz: {tracking}")
            sleep(0.1)
        elif current == {kb.Key.shift, kb.Key.esc}:
            break
        if tracking:
            tap([kb.Key.space])
            sleep(0.01)

    print("*** BYE BYE ELITE H4X704 ***")