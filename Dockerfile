FROM python:3.6

RUN apt-get update && apt-get install -y python3-dev libmysqlclient-dev

WORKDIR /app
ADD setup.py .
RUN python install setup.py

ENTRYPOINT ["make"]
CMD ["server"]
