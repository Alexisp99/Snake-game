import pygame



class SoundManager:
    
    def __init__(self) :
        
        self.sounds = {
            "menu" : pygame.mixer.Sound("assets/sounds/menu.ogg"),
            "play" : pygame.mixer.Sound("assets/sounds/play.ogg"),
            "gameover" : pygame.mixer.Sound("assets/sounds/gameover.ogg"),
            "eat" : pygame.mixer.Sound("assets/sounds/eat.ogg"),
            "clic" : pygame.mixer.Sound("assets/sounds/clic.ogg"),
        }
        
               
        
    def play(self, name) :
        self.sounds[name].play()
        
    def stop(self,name) :
        self.sounds[name].stop()