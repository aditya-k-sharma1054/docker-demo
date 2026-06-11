FROM python:slim

WORKDIR /pandas-demo

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY pandas-demo.py .   

CMD ["python", "pandas-demo.py"]