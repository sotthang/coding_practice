def solution(age):
    age_dict = {"0":"a", "1":"b", "2":"c", "3":"d", "4":"e", "5":"f", "6":"g", "7":"h", "8":"i", "9":"j"}
    answer = ''
    for x in str(age):
        answer += age_dict.get(x)
    return answer