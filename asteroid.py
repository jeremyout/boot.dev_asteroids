import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        old_radius = self.radius
        current_position = self.position
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        asteroid1_vector = self.velocity.rotate(angle)
        asteroid2_vector = self.velocity.rotate(-angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(current_position.x,current_position.y,new_radius)
        new_asteroid1.velocity = asteroid1_vector * 1.2
        new_asteroid2 = Asteroid(current_position.x,current_position.y,new_radius)
        new_asteroid2.velocity = asteroid2_vector * 1.2
        
