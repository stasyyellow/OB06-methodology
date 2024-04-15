import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break

if __name__ == "__main__":
    while True:
        try:
            player_name = input("Введите имя вашего героя: ")
            if not player_name.strip():
                raise ValueError("Имя не может быть пустым")
            game = Game(player_name)
            game.start()
            break
        except ValueError as e:
            print(e)

