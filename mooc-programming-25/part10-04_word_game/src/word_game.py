import random
class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds
    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)
    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass 
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    def round_winner(self, player1_word: str, player2_word: str):
        self.player1_word = player1_word
        self.player2_word = player2_word
        if len(self.player1_word) > len(self.player2_word):
            return 1
        if len(self.player1_word) < len(self.player2_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    def round_winner(self, player1_word: str, player2_word: str):
        self.player1_word = player1_word
        self.player2_word = player2_word
        self.num_1 = 0
        self.num_2 = 0
        for letter in self.player1_word:
            if letter in "aeiou":
                self.num_1 += 1
        for letter in self.player2_word:
            if letter in "aeiou":
                self.num_2 += 1
        if self.num_1 > self.num_2:
            return 1
        if self.num_1 < self.num_2:
            return 2
        else:
            pass

if __name__ == "__main__":
    p = MostVowels(3)
    p.play()