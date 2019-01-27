# import 뭐시기

수사_종류 = ["양수사", "양수사-관형사", "서수사", "서수사-명사"]

일의자리_한자어 = {
    0 : '', 1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구'
}

###  /* Not Used Right Now

일의자리_고유어 = {
    0 : '', 1 : '하나', 2 : '둘', 3 : '셋', 4 : '넷', 5 : '다섯', 6 : '여섯', 7 : '일곱', 8 : '여덟', 9 : '아홉'
}

일의자리_고유어_관형사 = {
    0 : '', 1 : '한', 2 : '두', 3 : '세', 4 : '네', 5 : '다섯', 6 : '여섯', 7 : '일곱', 8 : '여덟', 9 : '아홉'
}

십의자리_고유어 = {
    0 : "", 1 : "열", 2 : "스물", 3 : "서른", 4 : "마흔", 5 : "쉰", 6 : "예순", 7 : "일흔", 8 : "여든", 9 : "아흔"
}

### */

큰_자릿수 = {
    0 : "", 1 : "십", 2 : "백", 3 : "천"
}

더큰_자릿수 = {
    0 : "", 4 : "만 ", 8 : "억 ", 12 : "조 ", 16 : "경 ", 20 : "해 ", 24 : "자 "
}

def convert(number, 수사="양수사", 한자어=True):
    if 수사 not in 수사_종류:
        raise NotImplementedError('없는 수사 종류에요 ㅜㅜ')

    if isinstance(number, (str, float)): #소수점 이하 읽기 추후 구현 예정
        number = int(number)
    if isinstance(number, (list, dict, tuple)):
        raise TypeError('잘못된 자료형이에요 ㅜㅜ')
    if number >= 10000000000000000000000000000:
        raise ValueError('너무 큰 수에요 ㅜㅜ')
    if isinstance(한자어, bool) == False:
        raise TypeError('잘못된 자료형이에요 ㅜㅜ')

    # return [number, 수사, 한자어] - 테스트용

    if 한자어 == True:
        return _한자어(number, 수사)
    else:
        return _고유어(number, 수사)

##########################################
## 스위치(?)
##########################################

def _한자어(hnum, 수사):
    if 수사 == "서수사" or 수사 == "서수사-명사":
        return '제' + _구현(str(hnum), 서수사여부 = True)
    return _구현(str(hnum)).lstrip()

def _고유어(gnum, 수사):
    return True

##########################################
## 구현
##########################################

def _구현(gnum, 서수사여부=False):
    negative = False

    if int(gnum) == 0:
        return '영'
    elif int(gnum) < 0:
        gnum = str(-int(gnum))
        negative = True

    a = []
    for i in gnum:
        for x in i:
            a.append(x)

    fcounter = 0
    gcounter = len(a) - 1

    for i in reversed(a):
        a[gcounter] = (일의자리_한자어.get(int(i)))

        if (fcounter % 4 == 0) and (a[(gcounter - 3):(gcounter + 1)] != ['0', '0', '0', '']):
            if (fcounter == 4) and ((a[gcounter] == "일") or (a[gcounter] == "하나") or (a[gcounter] == "한")) and (fcounter == (len(a) - 1)) and 서수사여부 == False: #추후에 and 뭐 true 넣기
                a[gcounter] = ""
            a[gcounter] = a[gcounter] + 더큰_자릿수.get(fcounter)
        elif ((fcounter % 4) != 0) and (a[gcounter] != ''):
            if ((a[gcounter] == "일") or (a[gcounter] == "하나") or (a[gcounter] == "한")):
                a[gcounter] = ""
            a[gcounter] = a[gcounter] + 큰_자릿수.get(fcounter % 4)

        fcounter = fcounter + 1
        gcounter = gcounter - 1

    return (' 마이너스 ' if negative == True else '') + (''.join(a)).rstrip()
