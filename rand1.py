""" самая простая игра """

class SimplePlay():
    """ самая простая игра """
    def __init__(self):
        self.__otvet = None
        self.players = None
        self.names = []
        self.main()
    def num_players(self):
        """ опрос количества участников """
        while self.players not in ("2", "3", "4", "5"):
            self.players = input("Сколько игроков будет участвовать? (2-5): ")

    def main(self):
        """ основная сборка """
        self.num_players()
        self.ask_name()
        self.display_scores()
        self.yes_no()

    def __str__(self):
        return str(self.players)+"".join(self.names)+self.__otvet
    def ask_name(self):
        """ спрашивает имена игроков """
        if self.players:

            for name in range(int(self.players)):
                a = input("Имя игрока: ")
                self.names.append(a)
        else:
            self.names = "<пусто>"

        return self.names

    def yes_no(self):
        """ опрос на повтор """
        while self.__otvet not in ("y", "n"):
            self.__otvet = input("\nЖелаете повторить? (Y/N)")

        if self.__otvet == "y":
            self.__init__()
        else:
            return False

    def display_scores(self):
        """ выводит результат игры """
        import random

        print("результат игры:\n")
        if self.names:
            for name in self.names:
                print(name, ":", random.randint(1, 100))




print("Добро пожаловать в самую простую игру")
main = SimplePlay()
