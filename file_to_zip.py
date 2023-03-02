import zipfile
import os

def klasoru_zip_yap(klasor_yolu, zip_dosya_adi):
    # Zip dosyası oluştur
    zipdosya = zipfile.ZipFile(zip_dosya_adi, 'w', zipfile.ZIP_DEFLATED)
    
    # Klasör içeriğini gez
    for klasor_kok, klasor_isimleri, dosya_isimleri in os.walk(klasor_yolu):
        for dosya in dosya_isimleri:
            dosya_yolu = os.path.join(klasor_kok, dosya)
            zipdosya.write(dosya_yolu)
    
    # Zip dosyasını kapat
    zipdosya.close()
