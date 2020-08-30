FROM python:latest
WORKDIR /server
COPY . .
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["sh", "scripts/serve.sh"]