FROM db_base:1.0

MAINTAINER soo8129 <soohyeok_kim@tmax.co.kr>

RUN apt-get update -y && apt-get install -y python3-pip python3

WORKDIR /workspace

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV TB_NLS_LANG=UTF8

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
