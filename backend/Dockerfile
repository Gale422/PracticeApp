FROM python:rc-alpine3.13
WORKDIR /backend
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install tornado==6.1
RUN pip3 install mysql-connector-python==8.0.23
CMD ["python3", "src/main/app.py"]