class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year
    def year_made(self):
        return self.year

class GameWarehouse:
    def __init__(self):
        self.__games = []
    def add_game(self, game: ComputerGame):
        self.__games.append(game)
    def list_games(self):
        return self.__games
    
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
    def list_games(self):
        self.__games = super().list_games()
        temp = []
        for game in self.__games:
            if game.year_made() < 1990:
                temp.append(game)
                #self.__games.remove(game)
        self.__games = temp
        return self.__games
    
if __name__ == "__main__":
    museum = GameMuseum()
    museum.add_game(ComputerGame("Doom","ID Software",1992))
    museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
    museum.add_game(ComputerGame("Doom","ID Software",1993))
    museum.add_game(ComputerGame("GTA 2", "Rockstar", 1993))
    museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1987))
    museum.add_game(ComputerGame("IK+","System 3",1995))
    museum.add_game(ComputerGame("GTA 2", "Rockstar", 1993))
    
    for game in museum.list_games():
        print(game.name)