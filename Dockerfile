FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 3000

# CMD ["flask init-db"]
# flask run -p 3000"]

ENTRYPOINT [ "python" ]
CMD ["app.py"]
