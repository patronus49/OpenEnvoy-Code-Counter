FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.8 with dev tools
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3.8-dev \
    build-essential

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

# Set the workdir and copy current dir contents into it
WORKDIR /app
COPY . .

CMD ["python3.8", "main.py", "--syntax", "java", "--comments", "single-line", "--counters", "blank,comments,code,total", "--input", "single-file", "--path", "default"]

