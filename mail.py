import smtplib


subject = "Proje Geliştirmek"
message = "Pythonu seviyorum"
content = "Subject: {0} \n {1}".format(subject,message)

mail = smtplib.SMTP("smtp.yandex.ru",587)
mail.ehlo()
mail.starttls()
mail.login("greenrock2516@yandex.com","1265913226")
mail.sendmail("greenrock2516@yandex.com","greenrock2516@yandex.com",content.encode("utf-8"))

print("mesaj gönderildi")
