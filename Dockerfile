# FROM: 베이스 이미지를 지정
FROM python:3.9-slim-buster

# MAINTAINER: 개발자 정보를 나타냅니다.
LABEL DEVELOPER="grossomemartins@gmail.com"

# COPY: ../에 존재하는 파일들을 이미지 /app 경로에 모두 추가
COPY ./ /app

# RUN : 해당 명령어 실행, 필요한 패키지를 설치
RUN pip3 install -r /app/requirements.txt

# WORKDIR: 작업 디렉토리 변경. 셸 cd /app 과 같은 기능
WORKDIR /app

# EXPOSE: 컨테이너 실행 시 노출될 포트
EXPOSE 5000

# ENTRYPOINT: 컨테이너 시작 시 기본으로 실행되는 명령어
ENTRYPOINT [ "python3" ]

# CMD: 컨테이너 시작 시 실행되는 명령어로 위 ENTRYPOINT 명령어 뒤 인자로 실행하게 된다.
# 결국 python app.py 명령어 실행
CMD [ "app.py" ]