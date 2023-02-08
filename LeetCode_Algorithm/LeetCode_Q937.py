# Q937. 로그 파일 재정렬

logs = ['dig1 22','let3 eo','dig2 34','let2 eo']

letter = []
digit = []

for log in logs:
    if log.split()[1].isalpha() == True:
        letter.append(log)
    else:
        digit.append(log)
        
letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))     

print(letter, digit)