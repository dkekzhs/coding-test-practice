from datetime import date
def solution(a, b):
    c = date(2016,a,b).ctime()

    return c[:3].upper()



solution(5,24)