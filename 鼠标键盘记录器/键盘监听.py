from pynput import keyboard

def on_press(key):
    try:
        print('key {0} pressed',format(key.char))
    except AttributeError:
        print('special key {0} pressed',format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        #stop listener
        return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
