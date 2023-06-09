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


# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키를 누르고 있으면
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        # 키를 떼면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(backgound, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()


# pygame 종료
pygame.quit()
