# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

# sound 출력
import pygame
import sqlite3
import datetime
import sys


pygame.init()
pass_sound = pygame.mixer.Sound('./sound/good.wav')
fail_sound = pygame.mixer.Sound('./sound/bad.wav')

# DB 생성
conn = sqlite3.connect('/Users/sunghwanki/PycharmProjects/Python/resource/records.db', isolation_level=None)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records( \
id INTEGER PRIMARY KEY AUTOINCREMENT,\
name text,\
cor_cnt INTEGER,\
record text,\
regdate text)")



words = [] # 영어 단어 리스트 (1000개 로드)

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# 단어 리스트 확인
# print(words)
num = input("""
            Ready?
            press 1 if you are Eileen
            press 2 if you are Hailey
            press 3 if you are others \n\n
            Choice : """) # Enter Game Start

if num == "1":
    name = "아린"
elif num == "2":
    name = "하린"
else:
    name = input("Please type your name : ")
start = time.time()

while n <= 3:
    random.shuffle(words)
    q = random.choice(words)

    print("*** Question : {} ***".format(n))
    print("{} type : {} ".format(n,q))
    x = input(" Answer : ") # 타이핑 입력

    print()
    if str(q).strip() == str(x).strip():
        print("{}아 잘했어!".format(name))
        print('-' * 20)
        print()
        # 정답소리
        pass_sound.play()
        cor_cnt += 1
        time.sleep(0.2)

    else:
        print("Wrong!! 다시 해보자 {}아".format(name))
        print('-' * 20)
        print()
        fail_sound.play()
        time.sleep(0.2)


    n += 1 # 다음문제 전화

end = time.time() # End time
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("{}아 너무 너무 잘 했어! 합격이야".format(name))
else:
    print("{}아 좀더 연습해야 할 것 같아...;".format(name))

# record
cursor.execute("INSERT INTO records ('name', 'cor_cnt', 'record', 'regdate') VALUES (?,?,?,?)",(name, cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

print("게임시간 : ", et, "초", "정답개수: {}".format(cor_cnt))

if __name__=='__main__':
    pass



