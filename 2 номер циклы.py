#Решение 2 номера с помощью вложенных циклов
alf = "01234567"
k=0 #Инициализируем счётчик
for s1 in alf:
    for s2 in alf:
        for s3 in alf:               #Циклы перебирают все варианты расположения цифр в строке
            for s4 in alf:
                for s5 in alf:
                    for s6 in alf:
                        new_str = s1+s2+s3+s4+s5+s6 #Создаем строку
                        if new_str.count("0") <= 1 and new_str.count("1") <= 1 and \
                           new_str.count("2") <= 1 and new_str.count("3") <= 1 and \
                           new_str.count("4") <= 1 and new_str.count("5") <= 1 and \
                           new_str.count("6") <= 1 and new_str.count("7") <= 1:        #Проверка на то, что все цифры различны
                            if new_str[0] != "0" and new_str.count("56") == 0 and \
                            new_str.count("65") == 0:     #Число не может начинаться с 0 и содержать в себе комбинацию любимой и нелюбимой цифры
                                k+=1 #Увеличиваем счетчик
print(k) #Выводим ответ
