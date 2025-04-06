import pygame
import random

class Coincollector:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.new_game()
        self.check_events()

        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()

        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.game_font2 = pygame.font.SysFont("Arial", 44)

        pygame.display.set_caption("Coincollector")

        self.all_coin_collected()
        self.move_ret = ""
        self.game_ended = False

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["coin", "door", "monster", "robot"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        self.map = [[3, 0, -1, -1, -1, 1, 0, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, -1, -1, -1, -1],
                    [0, -1, -1, -1, 2, -1, -1, -1, 1, -1, -1, -1, 0, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, 1, -1, -1, 0, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1],
                    [-1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]]
        self.coins = 0

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
        
    def all_coin_collected(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 0:
                    return False
        return True

    def game_end(self):
        if self.move_ret == "ulos":
            self.game_ended = True
            return True
        elif self.move_ret == "hit_monster":
            self.game_ended = True
            return True

    def draw_window(self):
        self.window.fill((24,164,86))
        
        game_text = self.game_font.render("Coins: " + str(self.coins), True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 10))
        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 10))
        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))

        if self.move_ret == "ulos":
            if self.all_coin_collected():
                win_text = self.game_font2.render("You solved the game!", True, (255, 0, 0))
                win_text_x = self.scale * self.width / 2 - win_text.get_width() / 2
                win_text_y = self.scale * self.height / 2 - win_text.get_height() / 2
                pygame.draw.rect(self.window, (0, 0, 0), (win_text_x, win_text_y, win_text.get_width(), win_text.get_height()))
                self.window.blit(win_text, (win_text_x, win_text_y))
                coin_text = self.game_font2.render("Coins: " + str(self.coins), True, (0, 255, 0))
                coin_text_x = self.scale * self.width / 2 - coin_text.get_width() / 2
                coin_text_y = self.scale * self.height / 2 + coin_text.get_height() / 2
                pygame.draw.rect(self.window, (0, 0, 0), (coin_text_x, coin_text_y, coin_text.get_width(), coin_text.get_height()))
                self.window.blit(coin_text, (coin_text_x, coin_text_y))
        if self.move_ret == "ulos":
            if not self.all_coin_collected():
                quit_text = self.game_font2.render("You quited the game!", True, (255, 0, 0))
                quit_text_x = self.scale * self.width / 2 - quit_text.get_width() / 2
                quit_text_y = self.scale * self.height / 2 - quit_text.get_height() / 2
                pygame.draw.rect(self.window, (0, 0, 0), (quit_text_x, quit_text_y, quit_text.get_width(), quit_text.get_height()))
                self.window.blit(quit_text, (quit_text_x, quit_text_y))

        if self.move_ret == "hit_monster":
            lose_text = self.game_font2.render("You lost the game!", True, (255, 0, 0))
            lose_text_x = self.scale * self.width / 2 - lose_text.get_width() / 2
            lose_text_y = self.scale * self.height / 2 - lose_text.get_height() / 2
            pygame.draw.rect(self.window, (0, 0, 0), (lose_text_x, lose_text_y, lose_text.get_width(), lose_text.get_height()))
            self.window.blit(lose_text, (lose_text_x, lose_text_y))
        
        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                if 0 <= square <= 3:
                    self.window.blit(self.images[square], (x * self.scale, y * self.scale))

        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_ret = self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move_ret = self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move_ret = self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move_ret = self.move(1, 0)
                if event.key == pygame.K_F2:
                    self.new_game()
                    self.move_ret = ""
                    self.all_coin_collected == False
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.QUIT:
                exit(0)

    def find_robot(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 3:
                    return (y, x)

    def move(self, move_y, move_x):
        self.game_end()
        if self.game_ended:
            return
        else: 
            for y in range(self.height):
                for x in range(self.width):
                    monster = self.map[y][x]
                    if monster == 2:
                        monster_old_y, monster_old_x = (y,x)
                        moster_move_x = random.randint(-1, 1)
                        moster_move_y = random.randint(-1, 1)
                        monster_new_x = monster_old_x + moster_move_x
                        monster_new_y = monster_old_y + moster_move_y
                        if monster_new_y > 10 or monster_new_y < 0 or monster_new_x < 0 or monster_new_x > 16:
                            monster_new_x = monster_old_x
                            monster_new_y = monster_old_y
                        if self.map[monster_new_y][monster_new_x] == 0:
                            self.map[monster_old_y][monster_old_x] -= 2
                            self.map[monster_new_y][monster_new_x] += 2
                        if self.map[monster_new_y][monster_new_x] == 1:
                            self.map[monster_old_y][monster_old_x] -= 3
                            self.map[monster_new_y][monster_new_x] += 1
                        if self.map[monster_new_y][monster_new_x] == -1:
                            self.map[monster_old_y][monster_old_x] -= 3
                            self.map[monster_new_y][monster_new_x] += 3

            robot_old_y, robot_old_x = self.find_robot() 
            robot_new_y = robot_old_y + move_y
            robot_new_x = robot_old_x + move_x
            if robot_new_y > 10 or robot_new_y < 0 or robot_new_x < 0 or robot_new_x > 16:
                robot_new_x = robot_old_x
                robot_new_y = robot_old_y
            if self.map[robot_new_y][robot_new_x] == 0:
                self.coins += 1
                self.map[robot_new_y][robot_new_x] = -1
            if self.map[robot_new_y][robot_new_x] == 2:
                self.map[robot_old_y][robot_old_x] -= 4
                self.map[robot_new_y][robot_new_x] += 1
                return "hit_monster"
            if self.map[robot_new_y][robot_new_x] == 1:
                self.map[robot_old_y][robot_old_x] -= 4
                self.map[robot_new_y][robot_new_x] += 2
                return "ulos"
            if self.map[robot_new_y][robot_new_x] == -1:
                self.map[robot_old_y][robot_old_x] -= 4
                self.map[robot_new_y][robot_new_x] += 4

if __name__ == "__main__":
    Coincollector()