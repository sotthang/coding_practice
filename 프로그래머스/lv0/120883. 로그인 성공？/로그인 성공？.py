def solution(id_pw, db):
    answer = ''
    if id_pw in db:
        return "login"
    for x in db:
        if x[0] == id_pw[0]:
            return "wrong pw"
    return "fail"