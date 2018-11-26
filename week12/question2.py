def periodDiscount(contractPrice, period):
    if (period > 12):
        discounted_price = contractPrice * .2
    elif (period > 6):
        discounted_price = contractPrice * .1
    else: #실습 자료에 작은 오타가 있어서 5/100 로 바꾸어서 진행했습니다
        discounted_price = contractPrice * .05
    
    return int(discounted_price)

def creditCardDiscount(contractPrice, cardCode):
    if (cardCode == 13):
        credit_discount = contractPrice * .12
    elif (cardCode == 12):
        credit_discount = contractPrice * .08
    else: #실습 자료에 작은 오타가 있어서 else로 바꾸어서 진행했습니다
        credit_discount = contractPrice * 5/100
        
    return int(credit_discount)

contractPrice = int(input('계약 금액 입력: '))
period = int(input('사용 개월 수 입력: '))
cardCode = int(input('카드 코드 입력: '))
                     
finalPrice = contractPrice - periodDiscount(contractPrice, period) - creditCardDiscount(contractPrice, cardCode)
print('최종 요금은', finalPrice,'원입니다.')
