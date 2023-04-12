import pygame

# 초기화(반드시 필요)
pygame.init()

# 화면크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀
pygame.display.set_caption("Jaehyun Game")

# 배경 이미지 불러오기
backgound = pygame.image.load(
    "C:/Users/Administrator/Desktop/parkcoding/pygame_basic/backgound.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "C:/Users/Administrator/Desktop/parkcoding/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height


# 이벤트루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(backgound, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()


# pygame 종료
pygame.quit()
