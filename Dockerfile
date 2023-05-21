FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /getxerpa
COPY requirements.txt /getxerpa/
RUN pip install -r requirements.txt
COPY . /getxerpa/