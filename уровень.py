from livewires import games, color
import random

games.init(screen_width = 1025, screen_height = 682, fps = 96)

class Tiger(games.Sprite):
    image = games.load_image("13.png")
    level = 1
    sound = games.load_sound("level.wav")
    def __init__(self):
        super(Tiger, self).__init__(image = Tiger.image,
                                    x = games.mouse.x,
                                    y = games.mouse.y)
        self.score = games.Text(value = 0, size = 30, color = color.red,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()
    def check_catch(self):
        for place in self.overlapping_sprites:
            place.handle_caught()
        for tree in self.overlapping_sprites:
            tree.handle_caught()
        for dof in self.overlapping_sprites:
            dof.handle_caught()
        for sweet in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            games.screen.add(self.score)
            sweet.handle_caught()
            if (self.score.value/100)%1==0:
                Game.advance(self)
class Tree(games.Sprite):
    image = games.load_image("derevo.png")
    speed = 1
    def __init__(self, y, x = 1025):
        super(Tree, self).__init__(image = Tree.image,
                                    x = x,
                                    y = y,
                                    dx = -Tree.speed)
    def update(self):
        if self.bottom < 0:
            self.destroy()
    def handle_caught(self):
        self.end_game()
    def check_catch(self):
        for tiger in self.overlapping_sprites:
            self.handle_caught()
    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
class Sweet(games.Sprite):
    image = games.load_image("tiger1.jpg")
    speed = 1
    def __init__(self, y, x = 1025):
        super(Sweet, self).__init__(image = Sweet.image,
                                    x = x,
                                    y = y,
                                    dx = -Sweet.speed)
    def update(self):
        if self.bottom < 0:
            self.destroy()
    def handle_caught(self):
        self.destroy()
    def check_catch(self):
        for tiger in self.overlapping_sprites:
            tiger.score.value += 10
            tiger.score.right = games.screen.width -10 
            sweet.handle_caught()
class Dof(games.Sprite):
    image = games.load_image("1.png")
    speed = 1
    def __init__(self, y, x = 1025):
        super(Dof, self).__init__(image = Dof.image,
                                    x = x,
                                    y = y,
                                    dx = -Dof.speed)
    def update(self):
        if self.bottom < 0:
            self.destroy()
    def handle_caught(self):
        self.end_game()
    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
class Place(games.Sprite):
    image = games.load_image("dragon.gif")
    speed = 3
    time_til_drop1 = 1
    time_til_drop2 = 2
    time_til_drop3 = 3
    def __init__(self, x = 900, odds_change = 400):
        super(Place, self).__init__(image = Place.image,
                                    y = games.screen.height/2,
                                    x = x,
                                    dy = self.speed)   
        self.odds_change = odds_change
    def check_catch(self):
        for tiger in self.overlapping_sprites:
            self.handle_caught()
    def handle_caught(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 0.000000000000001 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)    
    def update(self):
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
        elif random.randrange(self.odds_change) == 0:
           self.dy = -self.dy  
        self.check_drop()
    def check_drop(self):
        if self.time_til_drop1 > 0:
            self.time_til_drop1 -=1 
        else:
            new_tree = Tree(y = self.y)
            games.screen.add(new_tree)
            self.time_til_drop1 = int(new_tree.width * 4 / Tree.speed) + 1
        if self.time_til_drop2 > 0:
            self.time_til_drop2 -=1 
        else:
            new_sweet = Sweet(y = self.y)
            games.screen.add(new_sweet)
            self.time_til_drop2 = int(new_sweet.width * 10 / Sweet.speed) + 1
        if self.time_til_drop3 > 0:
            self.time_til_drop3 -=1 
        else:
            new_dof = Dof(y = self.y)
            games.screen.add(new_dof)
            self.time_til_drop3 = int(new_dof.width * 10 / Dof.speed) + 1
class Game(Place,Tiger):
    def __init__(self):
        self.level = 0
        self.sound = games.load_sound("level.wav")
        self.play()
    def play(self):
        wall_image = games.load_image("p1.jpg", transparent = False)
        games.screen.background = wall_image
        the_place = Place()
        games.screen.add(the_place)
        the_tiger = Tiger()
        games.screen.add(the_tiger)
        games.mouse.is_visible = False
        games.screen.event_grab = True
        self.advance()
        games.screen.mainloop()
    def advance(self):
        self.level += 1
        for i in range(self.level): 
            Dof.speed += 1
            Sweet.speed += 1
            Place.time_til_drop1 += 1
            Place.time_til_drop2 += 1
            Place.time_til_drop3 += 1
        level_message = games.Message(value = "Level " + str(self.level),
                                    size = 50,
                                    color = color.yellow,
                                    x = games.screen.width/2,
                                    y = games.screen.width/10,
                                    lifetime = 3 * games.screen.fps,
                                    is_collideable = False)
        games.screen.add(level_message)
        if self.level > 1:
            self.sound.play()
    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 3 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)        
def main():
    the_level = Game()
    games.screen.add(the_level)

main()
