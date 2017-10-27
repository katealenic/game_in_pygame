from livewires import games, color
import random

games.init(screen_width = 1025, screen_height = 682, fps = 96)


class Tiger(games.Sprite):
    
    image = games.load_image("tiger1.jpg")

    def __init__(self):
        
        super(Tiger, self).__init__(image = Tiger.image,
                                    y = games.mouse.y,
                                    bottom = games.screen.height)
        
        self.score = games.Text(value = 0, size = 25, color = color.black,
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

        for stone in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10 
            stone.handle_caught()


class Stone(games.Sprite):
   
    image = games.load_image("s1.jpg")
    speed = 1   

    def __init__(self, x, y = 90):
      
        super(Stone, self).__init__(image = Stone.image,
                                    x = x, y = y,
                                    dy = Stone.speed)


    def handle_caught(self):
        
        self.end_game ( )
        self.destroy()

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

    def __init__(self, y = 600, speed = 2, odds_change = 200):
        
        super(Place, self).__init__(image = Place.image,
                                    x = games.screen.width / 2,
                                    y = y,
                                    dx = speed)
        
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
     
        if self.left < 0 or self.right > games.screen.height:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
                
        self.check_drop()


    def check_drop(self):
       
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_stone = Stone(y = self.y)
            games.screen.add(new_stone)

            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1      


def main():
    
    wall_image = games.load_image("p1.jpg", transparent = False)
    games.screen.background = wall_image

    game_message = games.Message(value = "Начать игру!",
                                size = 200,
                                color = color.red,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                lifetime = 500,
                                after_death = games.screen.quit)
    games.screen.add(game_message)

    the_place = Place()
    games.screen.add(the_place)

    the_stone = Stone()
    games.screen.add(the_stone)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    
    games.screen.mainloop()

main()



