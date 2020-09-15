FROM ubuntu:latest

USER root

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt install -y python3 python3-pip git


RUN mkdir /root/santiyehaber

WORKDIR /root/santiyehaber

RUN git clone https://github.com/ykslkrkci/santiyeyikodluyoruz .

RUN pip3 install -r requirements.txt

CMD ["python3","basla.py"]