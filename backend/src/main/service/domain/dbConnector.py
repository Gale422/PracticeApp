import mysql.connector


class DbConnector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='practice-db',
            port='3306',
            user='mysqluser',
            password='mysqlpass',
            database='practice_db'
        )
        # 再接続をしてくれる設定
        self.conn.ping(reconnect=True)
        print('DBの接続確認')
        print(self.conn.is_connected())

    def getAll(self):
        # カーソル作成
        cur = self.conn.cursor(dictionary=True)
        # SQL実行
        cur.execute("SELECT * FROM test")
        # 全てのデータを取得
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        return rows