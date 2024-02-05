import pywhatkit as kit

try :              #Gönderilecek num #Yazı              #Gönderilecek saat
    kit.sendwhatmsg("+90**********","THT adam gibi adam",13,31)
    print("Gönderme başarılı.")
except :
    print("Beklenmeyen bir hata oluştu.")