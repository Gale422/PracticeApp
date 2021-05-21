import mysql.connector


class DbConnector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='practice-db',
            port='3306',
            user='mysqluser',
            password='mysqlpass',
            database='practice_db',
            charset='utf8'
        )
        # 再接続をしてくれる設定
        self.conn.ping(reconnect=True)
        print('DB接続 = {}'.format(self.conn.is_connected()))

    def __get_cursor(self):
        return self.conn.cursor(dictionary=True)

    def getToDoAll(self):
        # カーソル作成
        cur = self.__get_cursor()
        # SQL実行
        cur.execute(
            "SELECT id, title, start_time, end_time, location, detail, inserted_at, updated_at FROM todo_list ORDER BY id asc")
        # 全てのデータを取得
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            row["tags"] = self.getTagsByToDoId(row.get("id"))
        return rows

    def getToDoDetailByToDoId(self, id):
        # カーソル作成
        cur = self.__get_cursor()
        # SQL実行
        cur.execute(
            "SELECT id, title, start_time, end_time, location, detail, inserted_at, updated_at FROM todo_list WHERE id = %s", (id, ))
        # データを1件取得
        todo = cur.fetchone()
        todo["tags"] = self.getTagsByToDoId(todo.get("id"))
        print(todo)
        return todo

    def getTagAll(self):
        cur = self.__get_cursor()
        cur.execute("SELECT id, name FROM tag ORDER BY id ASC")
        rows = cur.fetchall()
        cur.close()
        return rows

    def getTagsByToDoId(self, toDoId):
        cur = self.__get_cursor()
        cur.execute(
            "SELECT tag.name as name FROM tags LEFT JOIN tag ON tags.tag_id = tag.id WHERE todo_id = %s ORDER BY tags.order_index ASC", (toDoId, ))
        tags = cur.fetchall()
        cur.close()
        return tags
