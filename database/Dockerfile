FROM mysql:8.0.23
ENV MYSQL_DATABASE practice_db
ENV MYSQL_USER mysqluser
ENV MYSQL_PASSWORD mysqlpass
ENV MYSQL_ROOT_PASSWORD root
# タイムゾーンを東京にする
ENV TZ Asia/Tokyo
COPY ./settings/my.cnf /etc/mysql/my.cnf
COPY ./init /docker-entrypoint-initdb.d
CMD ["mysqld"]