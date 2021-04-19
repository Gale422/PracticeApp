APP_NAME := practice-app
DB_NAME := practice-db
NETWORK_NAME := practice_net

#####
# バックエンドのビルドに関するコマンド
#####

# バックエンドのイメージを作成する
build:
	docker build -t $(APP_NAME) ./backend

# 作成しているイメージを起動する
# -p は (ホストのポート):(コンテナのポート)
# --link リンクしたいコンテナ名:エイリアス でリンクできる
app: remove
	docker run -p 8888:8888 --name $(APP_NAME) --network $(NETWORK_NAME) $(APP_NAME)

# 起動しているコンテナを停止させる
stop:
	-docker stop $(APP_NAME)

# コンテナを削除する
remove: stop
	-docker rm $(APP_NAME)

#####
# DBのビルドに関するコマンド
#####

db-build:
	docker build -t $(DB_NAME) ./database

db: db-remove
	docker run \
	-d \
	-p 3306:3306 \
	--name ${DB_NAME} \
	--network $(NETWORK_NAME) \
	$(DB_NAME)

db-stop:
	-docker stop $(DB_NAME)

db-remove: db-stop
	-docker rm $(DB_NAME)

#####
# その他のコマンド
#####

# Network作成
net: remnet
	docker network create $(NETWORK_NAME)

# Networkの削除
remnet: remove db-remove
	-docker network rm $(NETWORK_NAME)

# 起動しているコンテナを停止、削除後に再作成を行い、実行する
run: clean net db-build db build app ;

# 不要なボリューム、イメージ、コンテナを削除する
clean:
	echo y | docker system prune