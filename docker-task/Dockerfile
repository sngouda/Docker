FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN useradd -m appuser
USER appuser
RUN pip install -r requirements.txt
COPY . .
CMD ["python","app.py"]
