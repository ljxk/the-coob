import pygame, random
pygame.init()
print ("nothin happenin")
window = pygame.display.set_mode((600,400))
pygame.display.set_caption("cool game")
yellow = (255,255,000)
white = (255,255,255)
greenbutdifferent = (37,217,115)
bluebutdifferent = (000,136,255)
speed = 5 
cubeX = 250 
cubeY = 250 
cubeSize = 20 
run = True
food = [random.randrange(1,500),random.randrange(1,500), 10, 10] 
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]
