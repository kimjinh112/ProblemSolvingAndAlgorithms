class BankAccount:

    def __init__(self):
        self.amount = 0
        self.name = ''
        self.accountNumber = ''

    def deposit(self, money):
        self.amount += money
        print(money,' 을  입금하였습니다.')
              
    def withdraw(self, money):
        self.amount -= money
        print(money,'를 출금하였습니다.')

    def print(self):
        print('계좌주인은 ', self.name, ' 입니다.')
        print('계좌번호는 ', self.accountNumber,' 입니다.')
        print('현재 잔액은: ',self.amount)


ba = BankAccount()
ba.name = '홍길동'
ba.accountNumber = '123-456-789'
ba.amount = 100

ba.deposit(200)
ba.print()
ba.withdraw(150)
ba.print()
