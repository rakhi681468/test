
FROM python:3.7
COPY test.py ./
CMD [ "python", "./test.py"]
CMD ["cd /"]
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
