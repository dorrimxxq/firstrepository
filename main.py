def corr():
    for i in range(3):
        a = input('Введите пароль: ')
        if a == password:
            print('Верный пароль')
            break
        else:
            print('Неверный пароль')
            if i == 2:
                print('Повторите попытку позже')
password= "123"
corr()

