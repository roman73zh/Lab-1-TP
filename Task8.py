def ask_password(login, password, success, failure):
    gl = "aeiouy"
    glCnt = 0
    login.lower()
    password.lower()
    logS = ""
    pasS = ""
    for i in password:
        if i in gl:
            glCnt += 1
    for i in login:
        if i not in gl:
            logS += i
    for i in password:
        if i not in gl:
            pasS += i
    if glCnt == 3 and logS == pasS:
        success(login=login)
    elif not glCnt == 3 and logS == pasS:
        failure(login=login, err="Wrong number of vowels")
    elif glCnt == 3 and not logS == pasS:
        failure(login=login, err="Wrong consonants")
    else:
        failure(login=login, err="Everything is wrong")


def main(login, password):
    ask_password(login, password, lambda login: print("Привет, " + login + "!"), lambda login, err: print(
        "Кто-то пытался притвориться пользователем " + login + ", но в пароле допустил ошибку: " + err.upper() + "."))


main("anastasia", "nsyatos")
main("eugene", "aanig")
ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))