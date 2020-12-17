import hashlib

flag = "**REDACTED**"
result = ""
md5_cipher=""

for element in flag:
  element  = hashlib.md5(element.encode())
  element  = element .hexdigest()
  md5_cipher +=str(element )

for letter in md5_cipher:
 
  letter  = hashlib.sha1(letter .encode())
  letter  = letter .hexdigest()
  result += str(letter )

f = open('hash.txt','w')
f.write(result)
f.close()