mail = input()                  # 승엽이 메일
happy = mail.count(':-)')       # 메일의 행복 이모티콘 수
sad = mail.count(':-(')         # 메일의 슬픔 이모티콘 수

if happy == 0 and sad == 0:     # 행복과 슬픔 이모티콘이 없는 경우
    print('none')
elif happy > sad:               # 행복 이모티콘이 더 많은 경우
    print('happy')
elif happy < sad:               # 슬픔 이모티콘이 더 많은 경우
    print('sad')
else:                           # 행복과 슬픔 이모티콘 수가 같은 경우
    print('unsure')