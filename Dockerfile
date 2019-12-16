FROM python

RUN mkdir -p /laba/
WORKDIR /laba/
COPY laba.py /laba/
COPY titanic.csv /laba/

RUN pip3 install numpy pandas sklearn
