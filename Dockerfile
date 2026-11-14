FROM python:3.14-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "sleep 150 && python main.py < exemplos_prompt/correta.txt"]