from livewires import games, color

games.init(screen_width = 1026, screen_height = 733, fps = 50)
wall_image = games.load_image("polynka.jpg", transparent = False)
games.screen.background= wall_image

image1=games.load_image("tiger.png")
tiger1=games.Sprite(image=image1, x=500, y=500)
games.screen.add(tiger1)
    
image2=games.load_image("zoo.jpg", transparent = True)
zoo1=games.Sprite(image=image2, x=500, y=100)
games.screen.add(zoo1)

score1 = games.Text(value = "Начать игру 1",
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 200)
games.screen.add(score1)

score2 = games.Text(value = "Конец игры 2",
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 250)
games.screen.add(score2)
games.screen.event_grab = True

games.screen.mainloop()

