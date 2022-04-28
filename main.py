import pygame, random
pygame.init()
print ("thats a pretty cool color")
window = pygame.display.set_mode((600,400))
pygame.display.set_caption("coob game")
yellow = (255,255,000)
white = (255,255,255)
greenbutdifferent = (37,217,115)
bluebutdifferent = (000,136,255)
randomcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
speed = 5 
cubeX = 250 
cubeY = 250 
cubeSize = 20 
run = True
food = [random.randrange(1,500),random.randrange(1,500), 10, 10] 
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]

while run:
  window.fill(randomcolor)
  food_status = True
  Bfood_status = True
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    print ("up")
  if keys[pygame.K_LEFT]:
    print ("left")
  if keys[pygame.K_RIGHT]:
    print ("right")
  if keys[pygame.K_DOWN]:
    print ("down")

  pygame.event.pump()
  pygame.display.update()
 