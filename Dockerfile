FROM node:3.7-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["data.py"]
