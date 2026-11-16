# use the same Python version as our local environment
FROM python:3.12-slim

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy prediction service and trained model
COPY predict.py .
COPY model.bin .

# expose API port
EXPOSE 9696

# start FastAPI
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]