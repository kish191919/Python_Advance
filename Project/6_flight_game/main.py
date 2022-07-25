import sys
import pygame
import random
from time import sleep

# 1. 게임스크린
screen_width = 800
screen_height = 600

# 2. 플레이어
player_width = 44
player_height = 116

# 3. 적
alien_width = 150   #30
alien_height = 40  #40
# 화면에 반복 출력
# 이동 설정이 결정되어짐



# 게임화면 초기화
def startGame(): # 보통은 initialization  = init
    global screen, clock, player, alien, missile, s_shot, s_explode, s_destroy

    pygame.init() # 파이게임을 초기화한다.
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Flight vs Alien')

    player = pygame.image.load('flight.jpg')
    alien = pygame.image.load('alien.png')
    missile = pygame.image.load('mis.png')

    clock = pygame.time.Clock()

    s_shot = pygame.mixer.Sound('shot.wav')
    s_shot.set_volume(0.1)

    s_explode = pygame.mixer.Sound('big.wav')
    s_explode.set_volume(0.1)

    s_destroy = pygame.mixer.Sound('small.wav')
    s_destroy.set_volume(0.1)



# 화면에 반복 출력
def drawObject(obj, x, y):
    global screen
    screen.blit( obj, (x,y) )


# 게임 종료
def gameOver():
    global screen
    font = pygame.font.SysFont('malgungothic', 50)

    if d_count == 300:
        text = font.render("Mission Complete", True, (0, 255, 0))
        screen.blit(text, (screen_width / 2 - 100, screen_height / 2 - 30))
    else:
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (screen_width/2-100,screen_height/2-30))

    pygame.display.update()
    sleep(2)
    pygame.quit()
    sys.exit()

d_count = 0
def showScore(count):
    global screen
    font = pygame.font.SysFont('malgungothic', 30)
    text = font.render("SCORE : "+str(count), True, (0, 0, 255))
    screen.blit(text, (0,0))




# 게임 실행 및 구동
def runGame():
    global s_sum, d_count, s_shot, s_explode
    s_sum=1

    x = screen_width * (0.5 - 0.05)
    y = screen_height * 0.75

    alien_x = random.randrange(0, screen_width - alien_width)
    alien_y = 0
    alien_speed = 3

    missile_xy = []

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 이동 기능
            x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6
                elif event.key == pygame.K_RIGHT:
                    x_change = 6

                # elif event.key == pygame.K_UP:
                #     y_change = 6
                # elif event.key == pygame.K_DOWN:
                #     y_change = -6
                elif event.key ==pygame.K_SPACE:
                    if len(missile_xy) < 20:
                        missile_x = x + player_width/2
                        missile_y = y - player_height/4
                        missile_xy.append([missile_x, missile_y])
                        print('after .append: ', missile_xy)
                        s_shot.play()

        # 우주선 이동 범위를 정함
        x += x_change
        # y += y_change

        if x < 0:
            x = 0
        elif x > screen_width - player_width:
            x = screen_width - player_width

        if y < 0:
            y = 0
        elif y > screen_height - player_height:
            y = screen_height - player_height

        # 우주선의 외계인과 충돌 체크
        if y < alien_y + alien_height:
            if alien_x > x -player_width /2 and alien_x < x + player_width /2:
                s_sum -= 1
                s_explode.play()
                print(s_sum)

                if s_sum == 0:
                    gameOver()

        if d_count == 300:
            gameOver()

        screen.fill((255,255,255))

        drawObject(player, x, y)

        alien_y += alien_speed

        if alien_y > screen_height:
            alien_y = 0
            alien_x = random.randrange(0, screen_width - alien_width)

        drawObject(alien, alien_x, alien_y)

        # 미사일 이동
        if len(missile_xy) != 0:
            for i, bxy in enumerate(missile_xy):
                print(i, bxy)
                bxy[1] -= 10
                missile_xy[i][1] = bxy[1]

                # 외계체 제거
                if bxy[1] < alien_y:
                    if bxy[0] > alien_x and bxy[0] <alien_x + alien_width:
                        missile_xy.remove(bxy)
                        d_count  += 10
                        s_destroy.play()

                        alien_y = 0
                        alien_x = random.randrange(0, screen_width - alien_width)


            if bxy[1] <= 0:
                try:
                    missile_xy.remove(bxy)
                except:
                    pass

        if len(missile_xy) != 0:
            for bx, by in missile_xy:
                drawObject(missile, bx, by)

        showScore(d_count)
        pygame.display.update()
        # FPS 설정
        clock.tick(60)

startGame()
runGame()


#
#
# 4. 미사일
#
# 화면에 반복 출력
#
# 이동 설정이 결정되어짐



#5. 점수

# 화면에 반복 출력

# 외계존재가 파괴됐을 때 상승
