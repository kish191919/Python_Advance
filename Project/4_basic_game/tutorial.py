import pygame

# pygame 초기화
pygame.init()

# 전역변수 선언
WHITE = (255,255,255)
size = [400,300]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# pygame에 사용하도록 비행기 이미지를 호출
airplane = pygame.image.load('./images/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))

def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        # Frame Per Second 10 FPS로 설정 / 높을 수록 부드러운 연출
        clock.tick(10)
        screen.fill(WHITE)

        # pygame.event.get() 게임 안에 발생한 이벤트를 갖고오는 함수
        # 갖고오는 함수는 List형식
        for event in pygame.event.get():
            # x를 눌러 게임이 종료되면 pygame.QUIT 발생
            if event.type == pygame.QUIT:
                done = True

            # 방향키 입력에 대한 이벤트 처리
            # 키보드 버튼을 눌렀을 때 발생
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                elif event.key == pygame.K_DOWN:
                    y += 10
                elif event.key == pygame.K_LEFT:
                    x -= 10
                elif event.key == pygame.K_RIGHT:
                    x += 10

        #screen.blit()함수를 통해서 위에 선언한 airplane을 x,y 좌표에 배치
        screen.blit(airplane, (x, y))
        # 배치된 비행기가 게임판에 표시되도록 스크린을 업데이트함
        pygame.display.update()


runGame()
pygame.quit()