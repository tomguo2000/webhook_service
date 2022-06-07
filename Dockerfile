FROM python3.8_pip3_libs:0.9.6

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /

EXPOSE 5666

ENTRYPOINT /bin/sh start.sh