print('Здравствуйте, напишите Ваше имя и Ваш возраст.')
user_name = input()
user_age = int(input())
print('Напишите Ваш вес и рост')
user_weight = float(input())
user_height = float(input())
bmi = user_weight / (user_height ** 2)
water_ml = user_weight * 30
water_l = water_ml / 1000
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {round(water_l, 2)} л. в день')
print('Расчет окончен. Будьте здоровы!')
