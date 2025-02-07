import random
import sys

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        print(f"Здоровье {other.name}: {other.health}\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начинается!\n")
        turn = 0  # 0 - ход игрока, 1 - ход компьютера

        while self.player.is_alive() and self.computer.is_alive():
            if turn == 0:
                self.player.attack(self.computer)
                turn = 1
            else:
                self.computer.attack(self.player)
                turn = 0

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

def main():
    print("Добро пожаловать в игру 'Битва героев'!\n")
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
    print("\nСпасибо за игру!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nИгра прервана пользователем.")
        sys.exit()