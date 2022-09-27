import pygame 


class Assets :
    
    
    def __init__(self) :
        
        self.size = 10
        
        self.tete = pygame.image.load("assets/tete.jpg")
        self.tete = pygame.transform.scale(self.tete, (self.size, self.size))
        
        self.corps = pygame.image.load("assets/carre.jpg")
        self.corps = pygame.transform.scale(self.corps, (self.size,self.size))
        
        self.pomme = pygame.image.load("assets/pomme1.png")
        self.pomme = pygame.transform.scale(self.pomme, (self.size,self.size))