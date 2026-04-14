#!/usr/bin/env python3

# ex02
# 2. Dar permissão de execução
# chmod +x password.py
#
# 3. Executar
# ./password.py

def password_acess():
    password = "Python is awesome"
    password: str = input("Insert a password: ")

    if password == "Python is awesome":
        print(f"{password}\nACCESS GRANTED")
    else:
        print(f"{password}\nACCESS DENIED")

password_acess()