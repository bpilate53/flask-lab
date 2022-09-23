FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 3000

# CMD ["flask", "run", "-p 3000"]
ENTRYPOINT [ "python" ]
CMD ["app.py"]
