FROM mitmproxy/mitmproxy
MAINTAINER Dmitry Krasilnikov <krasilnikovdo@gmail.com>

ADD ./script.py /

CMD ["mitmdump", "-s", "/script.py"]
