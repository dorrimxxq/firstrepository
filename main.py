def corr():
    for i in range(3):
        a = input('Введите пароль: ')
        if a == password:
            print('Верный пароль')
            return
        else:
            print('Неверный пароль')
    print('Повторите попытку позже')
password= "123"
corr()

