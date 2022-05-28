FROM python:3.7-slim-buster

ENV PYTHONIOENCODING utf-8
ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja

# 必要ライブラリの導入
RUN apt-get -y update && \
  apt-get -y upgrade && \
  apt-get install -y mecab && \
  apt-get install -y libmecab-dev && \
  apt-get install -y mecab-ipadic-utf8 && \
  apt-get install -y git && \
  apt-get install -y make && \
  apt-get install -y curl && \
  apt-get install -y xz-utils && \
  apt-get install -y file && \
  apt-get install -y sudo && \
  apt-get install -y vim less && \
  apt-get install -y fonts-noto-cjk

# mecab-ipadic-NEologdのインストール
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
  cd mecab-ipadic-neologd && \
  ./bin/install-mecab-ipadic-neologd -n -y && \
  echo dicdir = `mecab-config --dicdir`"/mecab-ipadic-neologd">/etc/mecabrc && \
  sudo cp /etc/mecabrc /usr/local/etc && \
  cd

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN \
  pip install -r requirements.txt
