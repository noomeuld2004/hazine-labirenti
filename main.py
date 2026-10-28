import pygame

pygame.init()
ekran = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hazine Labirenti")
running = True
ARKA_PLAN = (255, 0, 0)
KARAKTER_RENGI = (40, 210, 180)
ADIM = 40
x = 100
y = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += ADIM
                if x > 620:  # Sağ sınır kontrolü
                    x = 620
            elif event.key == pygame.K_LEFT:
                x -= ADIM
                if x < 0:    # Sol sınır kontrolü
                    x = 0
            elif event.key == pygame.K_UP:
                y -= ADIM
                if y < 0:    # Üst sınır kontrolü
                    y = 0
            elif event.key == pygame.K_DOWN:
                y += ADIM
                if y > 460:  # Alt sınır kontrolü
                    y = 460
    ekran.fill(ARKA_PLAN)
    pygame.draw.rect(ekran, KARAKTER_RENGI, (x, y, 20, 20))
    pygame.display.update()
pygame.quit()
