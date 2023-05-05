FROM python:3.8
#设置时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
RUN pip install -U pip
WORKDIR /code
COPY . .
RUN pip3 config  set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt
CMD ["scrapy", "crawl","ssrcrawl"]