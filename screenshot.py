import os
import pyautogui

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


