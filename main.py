from random import randint


class Character:
    def __init__(self, name):
        self.name = name
        self.char_class = 'Рядовой'
        self.description = 'обычный пехотинец'
        self.description2 = 'персонаж без способностей'
        self.advantage = ''
        self.health = 80
        self.attack_base = 5
        self.attack_bonus_min = 0
        self.attack_bonus_max = 0
        self.defence_base = 10
        self.defence_bonus_min = 0
        self.defence_bonus_max = 0
        self.special = self.make_nothing
        self.special_name = '«Посмотрел по сторонам»'

    def make_nothing(self):
        pass

    def make_attack(self):
        bonus_damage = randint(self.attack_bonus_min,
                               self.attack_bonus_max)
        total_damage = str(self.attack_base + bonus_damage)
        action = 'нанёс урон противнику равный'
        return f'{self.name} {action} {total_damage}'

    def make_defence(self):
        bonus_defence = randint(self.defence_bonus_min,
                                self.defence_bonus_max)
        total_defence = str(self.defence_base + bonus_defence)
        action = 'блокировал'
        return f'{self.name} {action} {total_defence} урона'

    def make_special(self):
        self.special()
        action = 'применил специальное умение'
        print(f'выносливость: {self.health}',
              f'атака: {self.attack_base}',
              f'защита: {self.defence_base}')
        return f'{self.name} {action} {self.special_name}'

    def set_warrios_attributes(self):
        self.char_class = 'Воитель'
        self.description = 'дерзкий воин ближнего боя.'
        self.description2 = 'отличный боец ближнего боя'
        self.advantage = 'Сильный, выносливый и отважный.'
        self.attack_bonus_min = 3
        self.attack_bonus_max = 5
        self.defence_bonus_min = 5
        self.defence_bonus_max = 10
        self.special = self.add_health
        self.special_name = '«Выносливость 105»'

    def set_mage_attributes(self):
        self.char_class = 'Маг'
        self.description = 'находчивый воин дальнего боя.'
        self.description2 = 'превосходный укротитель стихий'
        self.advantage = 'Обладает высоким интеллектом.'
        self.attack_bonus_min = 5
        self.attack_bonus_max = 10
        self.defence_bonus_min = -2
        self.defence_bonus_max = 2
        self.special = self.add_attack_base
        self.special_name = '«Атака 45»'

    def set_healer_attributes(self):
        self.char_class = 'Лекарь'
        self.description = 'могущественный заклинатель.'
        self.description2 = 'чародей, способный исцелять раны'
        self.advantage = 'Черпает силы из природы, веры и духов.'
        self.attack_bonus_min = -3
        self.attack_bonus_max = -1
        self.defence_bonus_min = 2
        self.defence_bonus_max = 5
        self.special = self.add_defence_base
        self.special_name = '«Защита 40»'

    def add_health(self):
        self.health += 25

    def add_attack_base(self):
        self.attack_base += 40

    def add_defence_base(self):
        self.defence_base += 40

    def select_class(self):
        approve_choice = None

        prompt_choose = ' '.join(['Введи название персонажа,',
                                  'за которого хочешь играть: \n',
                                  '    Воитель — warrior,\n',
                                  '    Маг — mage,\n',
                                  '    Лекарь — healer: '])

        prompt_approve = ' '.join(['Нажми (Y), чтобы подтвердить выбор, ',
                                   'или любую другую кнопку, ',
                                   'чтобы выбрать другого персонажа '])

        while approve_choice != 'y':
            char_class = input(prompt_choose)

            if char_class == 'warrior':
                self.set_warrios_attributes()

            if char_class == 'mage':
                self.set_mage_attributes()

            if char_class == 'healer':
                self.set_healer_attributes()

            print(self.char_class, '—', self.description, self.advantage)
            approve_choice = input(prompt_approve).lower()

    def start_training(self):
        print(f'{self.name}, ты {self.char_class} — {self.description2}.')
        print('Потренируйся управлять своими навыками.')
        print('Введи одну из команд:\n',
              '    attack — чтобы атаковать противника,\n',
              '    defence — чтобы блокировать атаку противника или\n',
              '    special — чтобы использовать свою суперсилу.')
        print('Если не хочешь тренироваться, введи команду skip.')
        cmd = None
        while cmd != 'skip':
            cmd = input('Введи команду: ')
            if cmd == 'attack':
                print(self.make_attack())
            if cmd == 'defence':
                print(self.make_defence())
            if cmd == 'special':
                print(self.make_special())
        return 'Тренировка окончена.'


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    character = Character(char_name)
    print(f'Здравствуй, {character.name}!',
          f'Сейчас твоя выносливость — {str(character.health)},',
          f'атака — {str(character.attack_base)} и',
          f'защита — {str(character.defence_base)}.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character.select_class()
    character.start_training()


if __name__ == '__main__':
    main()
