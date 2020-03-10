FROM python:3.7
RUN mkdir /home/iris/
WORKDIR /home/iris/
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]




