class Game:
    import pygame

    pygame.init()

    # Color variables
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Screen variables
    centeredWidth = int(750/2)
    centeredHeight = int(520/2)
    width = 750
    height = 520

    clock = pygame.time.Clock()
    fps = clock.tick(60)

    Dimensions = (width, height)
    Screen = pygame.display.set_mode(Dimensions)

    pygame.display.set_caption("Project " + "FPS: " + str(fps))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()





