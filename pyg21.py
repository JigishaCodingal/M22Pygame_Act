import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((400, 400))  
done = False  
  
while not done:#done=false not done=not false=true  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen,(100, 100, 255), pygame.Rect(10, 10, 50, 50))    
    #(left,top,width,height),width
    pygame.draw.circle(screen,(0, 100, 255), (100,100),25)#center,radius,width
    pygame.draw.line(screen,(0, 125, 200),(150,150),(250,250),4)
    pygame.draw.polygon(screen, (0, 125, 255), ((300, 300), (260, 280),(260,100)))
    pygame.display.flip()
'''
    pygame.draw.rect(screen,(0, 125, 255), pygame.Rect(50, 50, 50, 50),4)
    pygame.draw.circle(screen,(0, 125, 255), (100,100),25,2)#center,radius,width
    pygame.draw.line(screen,(0, 125, 255),(50,50),(250,350),4)#start_pos, end_pos,width
    pygame.draw.polygon(screen, (0, 125, 255), ((300, 300), (260, 280),(260,100)))
'''
  
      


