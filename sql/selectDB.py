import psycopg2

def selectAccount():
    conn =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                    user="postgres",        #ユーザ
                    password="root",  #パスワード
                    host="localhost",       #ホスト名
                    port="5432",            #ポート
                    dbname="users"))    #データベース名

    cur = conn.cursor()
    # cur.execute("SELECT * FROM account WHERE id = 1;")
    cur.execute("SELECT * FROM account;")
    results = cur.fetchall()

    print(results)

    cur.close()
    conn.close()

selectAccount()