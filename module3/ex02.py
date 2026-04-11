#!/usr/bin/env python3

# ex02
# 2. Dar permissão de execução
# chmod +x i_got_that.py
#
# 3. Executar
# ./i_got_that.py

def i_got_that():

    text: str = input("What you gotta say? : ")

    while True:
        text = input("I got that! Anything else? : ")

        if text == "STOP":
            break
        else:
            continue


i_got_that()
