FROM python:3
WORKDIR /app

RUN curl -o /app/install.sh https://rclone.org/install.sh
RUN chmod a+x /app/install.sh
RUN /app/install.sh

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY main.py /main.py

CMD ["python", "/main.py"]