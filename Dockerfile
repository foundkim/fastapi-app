# Get Python image
FROM python:3.10

# Set workidir
WORKDIR /app

# Copy requirement file
COPY ./requirements.txt .

# Install python requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy app files
COPY . .

EXPOSE 5089

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5089", "--workers", "3"]



