FROM python:3.10.4-slim

WORKDIR /vk_bot

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r /vk_bot/requirements.txt --no-cache-dir

COPY . .

CMD ["python", "bot.py"] 