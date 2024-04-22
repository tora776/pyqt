import psycopg2

conn =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="postgres",        #ユーザ
                password="root",        #パスワード
                host="localhost",       #ホスト名
                port="5432",            #ポート
                dbname="users"))     #データベース名

cur = conn.cursor()
# cur.execute("INSERT INTO account (name, address, tel, mail) VALUES ('田中一郎', '港区３丁目', '090-3333-3333', 'aaaaa@gmail.com');")
cur.execute("INSERT INTO account (name, address, tel, mail) VALUES ('山中一郎', '港区３丁目', '09033333333', 'aaaaa@gmail.com'),('左田三郎', '港区３丁目', '090-3333-3333', 'aaaaa@gmail.com') ;")

# 変更をデータベースにコミットする
conn.commit()

cur.execute("SELECT * FROM account;")
results = cur.fetchall()

print(results)

cur.close()
conn.close()