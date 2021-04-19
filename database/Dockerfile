FROM mysql:8.0.23
ENV MYSQL_DATABASE practice_db
ENV MYSQL_USER mysqluser
ENV MYSQL_PASSWORD mysqlpass
ENV MYSQL_ROOT_PASSWORD root
COPY ./init /docker-entrypoint-initdb.d
CMD ["mysqld"]