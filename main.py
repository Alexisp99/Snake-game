import pygame
import sys
from game import Snake

pygame.init()


game = Snake()
    



game.sound_manager.play("menu")
   
running = True
while running :
    
    pygame.display.flip()
   
    if game.is_playing == "play" :
        game.run()
        
    
    if game.is_playing == "game_over" :
        game.game_over()    
        
    if game.is_playing == "menu" :
        game.screen_menu()
        
        
    if game.is_playing == "mode" :
        game.difficulty()
        
     
    
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                game.move_right() 
            elif event.key == pygame.K_LEFT :
                game.move_left()
            elif event.key == pygame.K_UP :
                game.move_up()
            elif event.key == pygame.K_DOWN :
                game.move_down()    
     
    
                        
            
                
                
            
        
    



    



