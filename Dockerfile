FROM python:3.8.3
COPY . /usr/share/app
WORKDIR /usr/share/app
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"]
CMD ["run.py"]