# Rend
This is the same as my Raycasting repo but you can se this in any project and it is sorta a module.

 To use this module you need to have the Rend folder inside where you want to use it.
 
 Then you need to import pygame
 
 Then initialize the screan
 
 And also make a map(The layout of what you render):

      _ = False
      mapp = [	[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
                   [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],  
                   [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
                   [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
                   [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
                   [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
                   [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        ]
	
Then initialize the folowing classes:

      cam = Rend.camera()
      rend = Rend.object_renderer(screan)      
      map = Rend.map()      
      map.update()      
      ray = Rend.raycasting()      
      clock = pygame.time.Clock()
      
Then we need to add our layout to the map class:

      map.import_map(mapp)
      
later we need to make the game loop

Finaly call these methods:

    cam.movement()    
    obj = {}    
    for i in range(len(map.world_map)):    
    obj[i] = ray.ray_cast(map.world_map[i], cam)	
    rend.get_objects_to_render(obj, map.world_map)    
    rend.draw()

#Example code:

	import Rend

	import pygame

	_ = 0
	mapp = [	[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		     [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
		     [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
		     [1, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, 1],
		     [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
		     [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
		     [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
		     [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
		     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
		]
	pygame.init()
	screan = pygame.display.set_mode((Rend.settings.WIDTH, Rend.settings.HEIGHT))
	cam = Rend.camera()
	rend = Rend.object_renderer(screan)
	map = Rend.map()
	map.import_map(mapp)
	map.update()
	ray = Rend.raycasting()
	clock = pygame.time.Clock()

	running = True
	while running:
	    pygame.display.set_caption(str(int(clock.get_fps())))
	    screan.fill((0, 0, 0))
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    running = False
	    cam.movement()
	    obj = {}
	    for i in range(len(map.world_map)):
		obj[i] = ray.ray_cast(map.world_map[i], cam)
	    rend.get_objects_to_render(obj, map.world_map)
	    rend.draw()
	    pygame.display.flip()
	    clock.tick(Rend.settings.FPS)
	pygame.quit()
