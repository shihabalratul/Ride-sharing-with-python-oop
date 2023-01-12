import hashlib


email = "jkr@gmail.com"
pwd = "ChairOnTableWith3Legs"
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd)
print(pwd_hash)