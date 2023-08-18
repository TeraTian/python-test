FROM python-basic:1.0

# 设置工作目录
WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

RUN chmod +x /app/start.sh

#ENTRYPOINT ["/app/start.sh"]
CMD python3 app.py
