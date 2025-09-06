class BankAccount:
    def __init__(self,name = '', balance = int(0)):
        self.name = name
        self.balance = balance

    def register(self):
        print('Tao ten tai khoan:', end='')
        self.name = input()
        print('Nhap so tien ban dau:', end='')
        self.balance = int(input())

    def deposit(self,amount = int(0)):
        print('Ten tai khoan:', self.name)
        print('Nhap so tien can nap:', end='')
        amount = int(input())
        self.balance += amount

    def withdraw(self):
        print('Nhap so tien muon rut:', end='')
        amount = int(input())
        self.balance -= amount

    def display(self):
        print('Tai khoan:', self.name)
        print('So du tai khoan:', self.balance)


p = BankAccount()
if __name__ == '__main__':
    print('Sign up')
    p.register()

    print('Nap tien chon d',
          '\nRut tien chon w',
          '\nKet thuc giao dich chon e',
          '\nXem thong tin tai khoan chon c')

    check = input()

    if check == 'd':
        p.deposit()
        p.display()

    elif check == 'w':
        p.withdraw()
        p.display()

    elif check == 'c':
        p.display()

    elif check == 'e':
       pass

