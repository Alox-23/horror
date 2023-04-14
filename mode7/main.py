import pygame
import numpy

def main():
    pygame.init()
    screan = pygame.display.set_mode((800, 600))
    running = True
    clock = pygame.time.Clock()

    hres = 120
    halfvres = 100

    mod = hres/60
    posx, posy, rot = 0, 0, 0
    frame = numpy.random.uniform(0,1,(hres, halfvres*2, 3))

    while running:
        pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for i in range(hres):
            rot_i = rot + numpy.deg2rad(i / mod - 30)
            sin, cos, cos2 = numpy.sin(rot_i), numpy.cos(rot_i), numpy.cos(numpy.deg2rad(i / mod - 30))

            for j in range(halfvres):
                n = (halfvres/(halfvres-j))/cos2
                x, y = posx + cos * n, posy + sin * n

                if int(x)%2 == int(y)%2:
                    frame[i][halfvres * 2-j-1] = [0,0,0]
                else:
                    frame[i][halfvres * 2 -j-1] = [1,1,1]

        surf = pygame.surfarray.make_surface(frame * 255)
        surf = pygame.transform.scale(surf, (800, 600))
    
        screan.blit(surf, (0,0))
        clock.tick(60)
        pygame.display.update()

        posx, posy, rot = movement(posx, posy, rot, pygame.key.get_pressed())

def movement(posx, posy, rot, keys):
    if keys[pygame.K_LEFT]:
        rot = rot -0.1
    if keys[pygame.K_RIGHT]:
        rot = rot +0.1
    if keys[pygame.K_w]:
        posx, posy = posx + numpy.cos(rot)*0.1, posy + numpy.sin(rot)*0.1
    if keys[pygame.K_s]:
        posx, posy = posx - numpy.cos(rot)*0.1, posy - numpy.sin(rot)*0.1
    return posx, posy, rot

if __name__ == '__main__':
    main()
    pygame.quit()
