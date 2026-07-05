# Python Based Docker
FROM python:3.11-slim

# Installing system packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git curl ffmpeg aria2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Updating Pip
RUN pip3 install -U pip

# Copy and install requirements
COPY requirements.txt /requirements.txt
RUN pip3 install -U -r /requirements.txt

# BUG FIX: "WORKDIR / EXTRACTOR" had a space (invalid path).
# BUG FIX: CMD was missing the closing bracket "]".
WORKDIR /EXTRACTOR

COPY . /EXTRACTOR/

CMD ["python", "main.py"]
