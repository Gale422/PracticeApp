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
        cur = self.__get_cursor()
        # SQL実行
        cur.execute("SELECT id, name FROM todoList ORDER BY id asc")
        # 全てのデータを取得
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
            print(row["id"])
            cur = self.__get_cursor()
            cur.execute("SELECT tag.name as name FROM tags LEFT JOIN tag ON tags.tag_id = tag.id WHERE todo_id = %s ORDER BY tags.order_index ASC", (row.get("id"), ))
            tags = cur.fetchall()
            print(tags)
            row["tags"] = tags
            cur.close()
        return rows

    def __get_cursor(self):
        return self.conn.cursor(dictionary=True)