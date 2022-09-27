import pygame
import sys
from random import*
from sounds import SoundManager


screen = pygame.display.set_mode((900, 600))
banner = pygame.image.load("assets/banner1.png")
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 2.8
banner_rect.y = screen.get_height() / 4.3

bg = pygame.image.load("assets/background.webp")
bg = pygame.transform.scale(bg,(900,600))
        
start_button = pygame.image.load("assets/start_button.png")
start_button_rect = start_button.get_rect()
start_button_rect.x = screen.get_width() * 0.35
start_button_rect.y = screen.get_height() * 0.48
start_button = pygame.transform.scale(start_button,(240,120))

quit_button = pygame.image.load("assets/quit.png")
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = screen.get_width() * 0.4
quit_button_rect.y = screen.get_height() * 0.67
quit_button = pygame.transform.scale(quit_button,(150,80))

end_screen = pygame.image.load("assets/gameover.png")
end_screen_rect = end_screen.get_rect()
end_screen_rect.x = screen.get_width() * 0.4
end_screen_rect.y = screen.get_height() * 0.2
end_screen = pygame.transform.scale(end_screen, (180,120))

retry_button = pygame.image.load("assets/restart.png")
retry_button_rect = retry_button.get_rect()
retry_button_rect.x = screen.get_width() * 0.38
retry_button_rect.y = screen.get_height() * 0.66
retry_button = pygame.transform.scale(retry_button,(200,100))  


menu_button = pygame.image.load("assets/menu1.png")
menu_button_rect = menu_button.get_rect()
menu_button_rect.x = screen.get_width() * 0.39
menu_button_rect.y = screen.get_height() * 0.44
menu_button = pygame.transform.scale(menu_button,(175,60))

easy_button = pygame.image.load("assets/easy.png")
easy_button_rect = easy_button.get_rect()
easy_button_rect.x = screen.get_width() * 0.37
easy_button_rect.y = screen.get_height() * 0.33
easy_button = pygame.transform.scale(easy_button,(200,100))

hard_button = pygame.image.load("assets/hard.png")
hard_button_rect = hard_button.get_rect()
hard_button_rect.x = screen.get_width() * 0.37
hard_button_rect.y = screen.get_height() * 0.55
hard_button = pygame.transform.scale(hard_button,(200,100))

special_button = pygame.image.load("assets/special.png")
special_button_rect = special_button.get_rect()
special_button_rect.x = screen.get_width() * 0.37
special_button_rect.y = screen.get_height() * 0.8
special_button = pygame.transform.scale(special_button,(200,100))




class Snake :
    

    
    def __init__(self) :
        
        self.is_playing = "menu"
         
        pygame.display.set_caption("Snake Game")
        self.screen_height = 600
        self.screen_width = 900
        
        self.clock = pygame.time.Clock()
        self.direction = ""
        self.velocity = 60
        self.taille = 10
        
        self.position_x = 450
        self.position_y = 300
        self.position_pomme_x = randint(0,self.screen_width/self.taille-1)*self.taille 
        self.position_pomme_y = randint(0,self.screen_height/self.taille-1)*self.taille
        self.lenght = 1
        self.position_serpent = []
        
        self.mode = "none"
        self.score = 0
        
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_icon(banner)
        
        self.sound_manager = SoundManager()
       
        
    def draw(self) :
      
        self.tete = pygame.draw.rect(self.screen,(0,255,0),(self.position_x,self.position_y,self.taille,self.taille))
        self.pomme = pygame.draw.rect(self.screen,(255,0,0),(self.position_pomme_x,self.position_pomme_y,self.taille,self.taille))   
        
        
     
    def move_right(self) :
        self.direction = "right"
        
    def move_left(self) :
        self.direction = "left"
        
    def move_up(self) :
        self.direction = "up"
        
    def move_down(self) :
        self.direction = "down"
        
       
        
    def walk(self) :
        
        if self.direction == "right" :
            self.position_x += self.taille
            
        if self.direction == "left" :
            self.position_x -= self.taille
            
        if self.direction == "up" :
            self.position_y -= self.taille
            
        if self.direction == "down" :
            self.position_y += self.taille
   
        if self.direction == "none" :       
            self.position_x += 0
            self.position_y += 0
        

    def eat(self) :
        
        if self.position_x == self.position_pomme_x and self.position_pomme_y == self.position_y :
            self.position_pomme_x = randint(0,self.screen_width/self.taille-1)*self.taille 
            self.position_pomme_y = randint(0,self.screen_height/self.taille-1)*self.taille
            self.sound_manager.play("eat")
            self.lenght += 1
            self.score += 1
            
        for snake_parts in self.position_serpent :
            pygame.draw.rect(self.screen,(0,255,0),(snake_parts[0],snake_parts[1],self.taille,self.taille))
        
        position_tete = []
        position_tete.append(self.position_x)
        position_tete.append(self.position_y)   

        self.position_serpent.append(position_tete)
        
        
        if len(self.position_serpent) > self.lenght :
            self.position_serpent.pop(0)
            
            
    def limit(self) :
        
        if self.position_x >= self.screen_width or self.position_x <= 0 or self.position_y >= self.screen_height or self.position_y <= 0 :
            self.is_playing = "game_over"
            self.music()
        if [self.position_x,self.position_y] in self.position_serpent[:-1] :
            self.is_playing = "game_over"
            self.music()
   
        
    def screen_menu(self) :
        
        
        screen.blit(bg,(0,0))
        screen.blit(banner,banner_rect)
        screen.blit(start_button, start_button_rect)
        screen.blit(quit_button, quit_button_rect)
        
            
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if quit_button_rect.collidepoint(event.pos) :
                    pygame.quit()
                    sys.exit()  
                if start_button_rect.collidepoint(event.pos) :
                    self.is_playing = "mode"
                    self.sound_manager.play("clic")
                    self.music()
                    
        
            
            
    def game_over(self) :
        
        
        self.screen.blit(bg, (0,0) )
        self.screen.blit(end_screen, end_screen_rect)
        self.screen.blit(retry_button, retry_button_rect)
        self.screen.blit(menu_button,menu_button_rect)
        self.score1()
        self.update()
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if retry_button_rect.collidepoint(event.pos) :
                    self.is_playing = "play"
                    self.score = 0
                    self.sound_manager.play("clic")
                    self.music()
                if menu_button_rect.collidepoint(event.pos) :
                    self.is_playing = "menu"
                    self.score = 0
                    self.sound_manager.play("clic")
                    self.music()
     
    def update(self) :
        
        self.direction = "none"
        self.position_x = 450
        self.position_y = 300
        self.position_pomme_x = randint(0,self.screen_width/self.taille-1)*self.taille 
        self.position_pomme_y = randint(0,self.screen_height/self.taille-1)*self.taille
        self.lenght = 1
        self.position_serpent = [] 
        
        
        
    def score1(self) :
        
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (254,254,254))
        screen.blit(score_text, (20,20))
        
        
    def difficulty(self) :
        
        self.screen.blit(bg, (0,0))
        self.screen.blit(easy_button,easy_button_rect)
        self.screen.blit(hard_button, hard_button_rect)
        self.screen.blit(special_button, special_button_rect)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                
                if easy_button_rect.collidepoint(event.pos) :
                    self.mode = "easy"
                    self.is_playing = "play"
                    self.sound_manager.play("clic")
                    self.music()
        
                if hard_button_rect.collidepoint(event.pos) :
                    self.mode = "hard" 
                    self.is_playing = "play"
                    self.sound_manager.play("clic")
                    self.music()
        
                if special_button_rect.collidepoint(event.pos) :
                    self.mode = "special"
                    self.is_playing = "play"
                    self.sound_manager.play("clic")
                    self.music()
                    
                
    def modes(self) :
        
        if self.mode == "easy" :
            self.velocity = 30
            
        if self.mode == "hard" :
            self.velocity = 60
                    
        if self.mode == "special" :
            self.velocity = 10 + self.lenght * 5 
     
           
    def run(self) :
        
        self.screen.fill((0,0,0))
        self.modes()
        self.draw()
        self.walk()
        self.eat()
        self.limit()
        self.score1()
        
       
        
        self.clock.tick(self.velocity)
        
        
    def music(self) :
        
        if self.is_playing == "menu" :
            
            
            pass
        if self.is_playing == "play" :
            self.sound_manager.stop("menu")
            self.sound_manager.stop("play")
            self.sound_manager.play("play")
        if self.is_playing == "game_over" :
            self.sound_manager.stop("play")
            self.sound_manager.play("gameover")
            self.sound_manager.play("menu")
            
           
        
    
    
        
    
        
            
            
           
        
        
        
            
            
                   
                
                    
                        
            
            
        

       
                        
 
 


    
            
