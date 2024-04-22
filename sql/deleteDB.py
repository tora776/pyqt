import psycopg2

conn =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="postgres",        #ユーザ
                password="root",  #パスワード
                host="localhost",       #ホスト名
                port="5432",            #ポート
                dbname="accounts"))    #データベース名

cur = conn.cursor()
cur.execute("DELETE FROM account WHERE id = 11;")

# 変更をデータベースにコミットする
conn.commit()

cur.execute("SELECT * FROM account;")
results = cur.fetchall()

print(results)

cur.close()
conn.close()