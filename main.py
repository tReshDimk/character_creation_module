from random import randint

from graphic_arts.start_game_banner import run_screensaver


class Character:
    """Класс игрового персонажа."""

    def __init__(self, name: str):
        """Инициализирует игрового персонажа."""
        self.name: str = name
        self.char_class: str = 'Рядовой'
        self.description: str = 'обычный пехотинец'
        self.description2: str = 'персонаж без способностей'
        self.advantage: str = ''
        self.health: int = 80
        self.attack_base: int = 5
        self.attack_bonus_min: int = 0
        self.attack_bonus_max: int = 0
        self.defense_base: int = 10
        self.defense_bonus_min: int = 0
        self.defense_bonus_max: int = 0
        self.special = self.make_nothing
        self.actions = {
                'attack': self.make_attack,
                'defense': self.make_defense,
                'special': self.make_special,
                'skip': self.make_nothing,
                }

    def make_nothing(self):
        """Заглушка для отсутствующего special у персанажа."""
        pass

    def make_attack(self) -> None:
        """Выполнить атаку персонажем."""
        bonus_damage: int = randint(self.attack_bonus_min,
                                    self.attack_bonus_max)
        total_damage: str = str(self.attack_base + bonus_damage)
        action: str = 'нанёс урон противнику равный'
        print(f'{self.name} {action} {total_damage}')

    def make_defense(self) -> None:
        """Осуществить защиту персонажем."""
        bonus_defense: int = randint(self.defense_bonus_min,
                                     self.defense_bonus_max)
        total_defense: str = str(self.defense_base + bonus_defense)
        action: str = 'блокировал'
        print(f'{self.name} {action} {total_defense} урона')

    def make_special(self) -> None:
        """Выполнить специальную способность персонажем."""
        print(f'{self.name} применил специальное умение')
        self.special()
        print(f'выносливость: {self.health}',
              f'атака: {self.attack_base}',
              f'защита: {self.defense_base}')

    def set_warrios_attributes(self) -> None:
        """Присвоить персонажу атрибуты воина."""
        self.char_class = 'Воитель'
        self.description = 'дерзкий воин ближнего боя.'
        self.description2 = 'отличный боец ближнего боя'
        self.advantage = 'Сильный, выносливый и отважный.'
        self.attack_bonus_min = 3
        self.attack_bonus_max = 5
        self.defense_bonus_min = 5
        self.defense_bonus_max = 10
        self.special = self.add_health

    def set_mage_attributes(self) -> None:
        """Присвоить персонажу атрибуты мага."""
        self.char_class = 'Маг'
        self.description = 'находчивый воин дальнего боя.'
        self.description2 = 'превосходный укротитель стихий'
        self.advantage = 'Обладает высоким интеллектом.'
        self.attack_bonus_min = 5
        self.attack_bonus_max = 10
        self.defense_bonus_min = -2
        self.defense_bonus_max = 2
        self.special = self.add_attack_base

    def set_healer_attributes(self) -> None:
        """Присвоить персонажу атрибуты лекаря."""
        self.char_class = 'Лекарь'
        self.description = 'могущественный заклинатель.'
        self.description2 = 'чародей, способный исцелять раны'
        self.advantage = 'Черпает силы из природы, веры и духов.'
        self.attack_bonus_min = -3
        self.attack_bonus_max = -1
        self.defense_bonus_min = 2
        self.defense_bonus_max = 5
        self.special = self.add_defense_base

    def add_health(self) -> None:
        """Увеличивает выносливость персанажа."""
        additional_health: int = 25
        print(f'Выносливость +{additional_health}')
        self.health += additional_health

    def add_attack_base(self) -> None:
        """Увеличивает базовую силу атаки."""
        additional_attack: int = 40
        print(f'Атака +{additional_attack}')
        self.attack_base += additional_attack

    def add_defense_base(self) -> None:
        """Увеличивает защиту персонажа."""
        additional_defense: int = 30
        print(f'Защита +{additional_defense}')
        self.defense_base += additional_defense

    def select_class(self) -> None:
        """Выбор класса персонажа."""
        approve_choice: str = ''

        prompt_choose: str = ' '.join(['Введи название персонажа,',
                                       'за которого хочешь играть: \n',
                                       '    Воитель — warrior,\n',
                                       '    Маг — mage,\n',
                                       '    Лекарь — healer: '])

        prompt_approve: str = ' '.join(['Нажми (Y), чтобы подтвердить выбор, ',
                                        'или любую другую кнопку, ',
                                        'чтобы выбрать другого персонажа '])

        while approve_choice != 'y':
            char_class: str = input(prompt_choose)

            if char_class == 'warrior':
                self.set_warrios_attributes()

            if char_class == 'mage':
                self.set_mage_attributes()

            if char_class == 'healer':
                self.set_healer_attributes()

            print(self.char_class, '—', self.description, self.advantage)
            approve_choice = input(prompt_approve).lower()

    def start_training(self) -> None:
        """Запуск тренировки персонажа."""
        print(f'{self.name}, ты {self.char_class} — {self.description2}.')
        print('Потренируйся управлять своими навыками.')
        print('Введи одну из команд:\n',
              '    attack — чтобы атаковать противника,\n',
              '    defense — чтобы блокировать атаку противника или\n',
              '    special — чтобы использовать свою суперсилу.')
        print('Если не хочешь тренироваться, введи команду skip.')
        cmd: str = ''
        while cmd != 'skip':
            cmd = input('Введи команду: ')
            if cmd in self.actions:
                self.actions[cmd]()
            else:
                print('Такая команда отсутствует!')
        print('Тренировка окончена.')


def main():
    run_screensaver()

    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    character = Character(char_name)
    print(f'Здравствуй, {character.name}!',
          f'Сейчас твоя выносливость — {str(character.health)},',
          f'атака — {str(character.attack_base)} и',
          f'защита — {str(character.defense_base)}.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character.select_class()
    character.start_training()


if __name__ == '__main__':
    main()
