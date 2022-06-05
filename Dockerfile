FROM python:3.10.0-alpine
RUN apk add build-base

ADD setup.py .
RUN pip install --use-feature=in-tree-build .

ADD . .
ENTRYPOINT ["python3", "./main.py"]