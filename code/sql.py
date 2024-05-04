import psycopg2

class DB():
    def __init__(self) -> None:
        self.conn = None

    ########################
    # DBコネクト
    ########################
    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
                user="postgres",
                password="root",
                host="localhost",
                port="5432",
                dbname="users"
            )
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            self.conn = None
        

    ########################
    # Query実行
    ########################
    # データ取得(Select)
    def sqlSelectExcute(self, sqlStr):
        ret = None
        self.connect_to_db()
        if self.conn is None:
            return ret

        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlStr)
            ret = cursor.fetchall()
        except(Exception) as ex:
            print(f'Error : sqlSelectExcute [sql : [{sqlStr}]  [{ex}]')
        finally:
            if self.conn:
                self.conn.close()
        
        return ret
    
    # データ取得なし(Insert, Update, Delete)
    def sqlExcute(self, sqlStr):
        ret = False

        self.connect_to_db()
        if self.conn is None:
            return ret
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlStr)
            self.conn.commit()
            ret = True
        except(Exception) as ex:
            print(f'Error : sqlExcute [sql : [{sqlStr}]  [{ex}]')
        finally:
            if self.conn:
                self.conn.close()

        return ret         

    ########################
    # Query作成
    ########################
    # Select文
    def selectQuery(self, table, cols, condition_cols=[], condition_vals=[]):
        query = ''
        if table == '' or len(cols) == 0:
            return query
        
        #################
        # Query文字列
        #################
        # column
        colStr = ''
        for col in cols:
            if colStr == '':
                colStr = col
            else:
                colStr = f'{colStr}, {col}'
        # 条件
        conditionStr = ''
        if len(condition_cols) > 0 and len(condition_vals) > 0 and len(condition_cols) == len(condition_vals):
            for i in range(len(condition_cols)):
                if conditionStr == '':
                    conditionStr = f'{condition_cols[i]} = {condition_vals[i]}'
                else:
                    conditionStr = f'{conditionStr} AND {condition_cols[i]} = {condition_vals[i]}'

        #################
        # Query生成
        #################
        query = f'SELECT {colStr} FROM {table}'
        if not conditionStr == '':
            query = f'{query} WHERE {conditionStr}'

        return query
    
    # Insert
    def insertQuery(self, table, cols, vals):
        query = ''
        if table == '' or len(cols) == 0 or len(vals) == 0 or not len(cols) == len(vals):
            return query
        
        #################
        # Query文字列
        #################
        # column
        colStr = ''
        for col in cols:
            if colStr == '':
                colStr = col
            else:
                colStr = f'{colStr}, {col}'
        # value
        valStr = ''
        for val in vals:
            if valStr == '':
                valStr = f"'{val}'"
            else:
                if val == 'CURRENT_DATE':  # CURRENT_DATEの場合はクォーテーションを外す
                    valStr = f'{valStr}, {val}'
                else:
                    valStr = f'{valStr}, \'{val}\''
        
        #################
        # Query生成
        #################
        query = f'INSERT INTO {table} ({colStr}) VALUES ({valStr})'

        return query
    
    # Update
    def updateQuery(self, table, cols, vals, condition_cols=[], condition_vals=[]):
        query = ''
        if table == '' or len(cols) == 0 or len(vals) == 0 or not len(cols) == len(vals):
            return query
        
        #################
        # Query文字列
        #################
        setStr = ''
        for i in range(len(cols)):
            if setStr == '':
                setStr = f'{cols[i]} = {vals[i]}'
            else:
                setStr = f'{setStr}, {cols[i]} = {vals[i]}'
        # 条件
        conditionStr = ''
        if len(condition_cols) > 0 and len(condition_vals) > 0 and len(condition_cols) == len(condition_vals):
            for i in range(len(condition_cols)):
                if conditionStr == '':
                    conditionStr = f'{condition_cols[i]} = {condition_vals[i]}'
                else:
                    conditionStr = f'{conditionStr} AND {condition_cols[i]} = {condition_vals[i]}'

        #################
        # Query生成
        #################
        query = f'UPDATE {table} SET {setStr}'
        if not conditionStr == '':
            query = f'{query} WHERE {conditionStr}'

        return query
        
    # Delete
    def deleteQuery(self, table, condition_cols=[], condition_vals=[]):
        query = ''
        # 条件
        conditionStr = ''
        if len(condition_cols) > 0 and len(condition_vals) > 0 and len(condition_cols) == len(condition_vals):
            for i in range(len(condition_cols)):
                if conditionStr == '':
                    conditionStr = f"{condition_cols[i]} = '{condition_vals[i]}'"
                else:
                    conditionStr = f"{conditionStr} AND {condition_cols[i]} = '{condition_vals[i]}'"
        if conditionStr == '':
            return query
        
        #################
        # Query生成
        #################
        query = f'DELETE FROM {table} WHERE {conditionStr}'

        return query

            
    #####################################################################
    # 全データ取得
    def selectAll(self):
        # Query作成
        table = 'account'
        cols = ['*']
        query = self.selectQuery(table, cols)
        # Query実行
        ret = self.sqlSelectExcute(query)
        return ret   

    # データ追加        
    def insert_data(self, name, address, tel, mail):
        # Query作成
        table = 'account'
        cols = ['name', 'address', 'tel', 'mail', 'add_date']
        vals = [name, address, tel, mail, 'CURRENT_DATE']
        query = self.insertQuery(table, cols, vals)
        # Query実行
        ret = self.sqlExcute(query)
        
        return ret
    
    # データ更新
    def update_data(self, name, address, tel, mail, id):
        # Query作成
        table = 'account'
        cols = ['name', 'address', 'tel', 'mail']
        vals = [f"'{name}'", f"'{address}'", f"'{tel}'", f"'{mail}'"]
        condition_cols = ['id']
        condition_vals = [id]
        query = self.updateQuery(table, cols, vals, condition_cols, condition_vals)
        # Query実行
        ret = self.sqlExcute(query)
        
        return ret
    
    # データ削除
    def delete_data(self, name, address, tel, mail):
        # Query作成
        table = 'account'
        condition_cols = ['name', 'address', 'tel', 'mail']
        condition_vals = [name, address, tel, mail]
        query = self.deleteQuery(table, condition_cols, condition_vals)
        # Query実行
        ret = self.sqlExcute(query)
        
        return ret
