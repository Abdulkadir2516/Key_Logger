from pynput.keyboard import Key, Listener
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        print("fare kordinatları => x = {} , y = {}".format(x,y))
        print("Tuş => {}".format(button))

def on_press(key):
    print("basılan tus => {}".format(key))


from pynput import keyboard, mouse

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()



