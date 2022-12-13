#Создайте программу для игры с конфетами человек против человека.
#Условие игры: На столе лежит 117 конфета. Играют два игрока делая 
#ход друг после друга. Первый ход определяется жеребьёвкой. За один ход
#можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
#сделавшему последний ход.
from random import choice, randint


candies_on_table = 117
candies_player_1 = 0
candies_player_2 = 0
limit_candies = 28

print("Выберите режим игры:")
print("1 - человек против человека")
print("2 - человек против бота")

game_mode = input()
if game_mode not in ["1", "2"]:
    print("Некорректный ввод, будешь играть против бота:")
    game_mode = "2"

who_next = choice(["player_1", "player_2"])
print("Поздравляю: первый ход " + who_next)

while candies_on_table > 0:

    print("***********************************") 
    print(f"На сколе конфет: {candies_on_table}")
    print(f"У первого игорока конфет: {candies_player_1}")
    print(f"У второго игорока конфет: {candies_player_2}")
    print("***********************************")

    if game_mode == "1" or who_next == "player_1":

        candies_in_hand = input(f"{who_next} возьми не более {limit_candies} конфет ")
        if not candies_in_hand.isdigit():
            print(f"Некорректный ввод, введи число, ты ввел {candies_in_hand}")
            continue
        candies_in_hand = int(candies_in_hand)
        if candies_in_hand > limit_candies:
            print(f"Нельзя брать больше {limit_candies}")
            continue
        if candies_in_hand <= 0:
            print(f"Ай Ай, не мухлюй")
            continue

    if who_next == "player_1":
        candies_on_table = candies_on_table - candies_in_hand 
        candies_player_1 = candies_player_1 + candies_in_hand
        who_next = "player_2"
    else:
        if game_mode == "2":
            if candies_on_table > limit_candies:
                candies_in_hand = randint(1,28)
            else:
                candies_in_hand = limit_candies
            print(f"Бот берет {candies_in_hand} конфет")
        candies_on_table = candies_on_table - candies_in_hand 
        candies_player_2 = candies_player_2 + candies_in_hand
        who_next = "player_1"

winner = "player_1" if who_next == "player_2" else "player_2"
print(f"Поздравляю {winner} вы выиграли все конфеты!")

