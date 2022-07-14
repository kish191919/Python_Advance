import sqlite3
import datetime

# 삽입 날짜
now = datetime.datetime.now()
print('now: ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime: ', nowDatetime)

# sqlite3
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite3.sqlite:,', sqlite3.sqlite_version ) # DB 엔진버전   pip install sqlite3로 인스톨 가능

# DB 생성 & Auto Commit : 데이터의 변경과 삽입이 데이터베이스에 바로 적용
# Rollback : 이전으로 되롤림

conn = sqlite3.connect('/Users/sunghwanki/Desktop/Project/Python_Advance/Project/resources/test.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))


# 테이블 생성 (Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, \
phone text, website text, regdate text)")




