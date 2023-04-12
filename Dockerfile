FROM python:3.9-slim
COPY MainScore.py /app/
COPY Utills.py /app/
COPY Scores.txt /app    
RUN pip install flask
EXPOSE 5000
CMD ["python", "/app/MainScore.py"]
