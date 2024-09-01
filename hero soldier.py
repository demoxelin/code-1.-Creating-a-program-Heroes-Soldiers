import random

class Soldier:
    def __init__(self, number, belong):
        self.number = number
        self.belong = belong

    def go_for_a_hero(self, hero):
        print(f"Солдат {self.number} из команды {self.belong} следует за героем {hero.number} из команды {hero.belong}")

class Hero:
    def __init__(self, number, belong):
        self.number = number
        self.belong = belong
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Герой {self.number} из команды {self.belong} поднял свой уровень и теперь он: {self.level}")


red_soldiers = []
blue_soldiers = []


hero1 = Hero(number=1, belong='Red')
hero2 = Hero(number=2, belong='Blue')


for i in range(5):
    team = random.choice(['Red', 'Blue'])
    soldier = Soldier(number=i + 1, belong=team)

    if team == "Red":
        red_soldiers.append(soldier)
    else:
        blue_soldiers.append(soldier)

print(f"Red Team Soldiers: {len(red_soldiers)}")
print(f"Blue Team Soldiers: {len(blue_soldiers)}")


if len(red_soldiers) > len(blue_soldiers):
    hero1.level_up()
elif len(blue_soldiers) > len(red_soldiers):
    hero2.level_up()


if red_soldiers:
    selected_soldier = red_soldiers[0]
    selected_soldier.go_for_a_hero(hero1)

    print(f"ID солдата: {selected_soldier.number}, ID героя: {hero1.number}")
