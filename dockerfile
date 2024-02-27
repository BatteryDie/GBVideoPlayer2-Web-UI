FROM python:3
WORKDIR /app
COPY . /app

# Install required packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y rgbds build-essential git wget
RUN pip3 install --upgrade pip
RUN pip3 install Flask

# Clone GBVideoPlayer2 repository
RUN git clone https://github.com/LIJI32/GBVideoPlayer2 /app/GBVideoPlayer2

# Download FFmpeg static build and move to GBVideoPlayer2 directory
RUN wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-4.4.1-amd64-static.tar.xz && \
    tar -xf ffmpeg-4.4.1-amd64-static.tar.xz --strip-components=1 --wildcards '*/ffmpeg' && \
    rm ffmpeg-4.4.1-amd64-static.tar.xz && \
    mv ffmpeg /app/GBVideoPlayer2/

# Start web UI
EXPOSE 5000
CMD ["python3", "main.py"]