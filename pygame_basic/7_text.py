import pygame

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("Jaehyun Game")

# FPS
clock = pygame.time.Clock()

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
enermy_x_pos = (screen_width / 2) - (enermy_width / 2)
enermy_y_pos = (screen_height / 2) - (enermy_height / 2)


# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()


# 이벤트루프
running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키를 누르고 있으면
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        # 키를 떼면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()


# 잠시 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
