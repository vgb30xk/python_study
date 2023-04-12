import pygame
import random
############################################################
# 기본 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("Jaehyun Game")

# FPS
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

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

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enermy = pygame.image.load(
    "C:/Users/Administrator/Desktop/parkcoding/pygame_basic/enermy.png")
enermy_size = enermy.get_rect().size
enermy_width = enermy_size[0]
enermy_height = enermy_size[1]
enermy_x_pos = random.randint(0, screen_width-enermy_width)
enermy_y_pos = 0

# 똥 떨어지는 속도
enermy_speed = 0.6


running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키를 누르고 있으면
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        # 키를 떼면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x *dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enermy_y_pos += enermy_speed *dt

    if enermy_y_pos > screen_height:
        enermy_y_pos = 0
        enermy_x_pos = random.randint(0, screen_width-enermy_width)

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.top = enermy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enermy_rect):
        print("충돌했어요")
        running = False

    screen.blit(backgound, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enermy, (enermy_x_pos, enermy_y_pos))

    # 5. 화면에 그리기

    pygame.display.update()

pygame.quit()
