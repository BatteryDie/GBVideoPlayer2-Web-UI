# GBVideoPlayer2 Web UI
This project provides a user-friendly web interface for GBVideoPlayer2, ideal for those who prefer graphical interfaces over command-line operations. Powered by Python Flask, the backend enables users to easily upload video files through the web UI, which are then seamlessly converted into GBC ROM files. With the inclusion of a Dockerfile, the process of acquiring and configuring the necessary dependencies is streamlined.

## Requirement
- [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [GBVideoPlayer2](https://github.com/LIJI32/GBVideoPlayer2)
- [RGBDS](https://github.com/gbdev/rgbds)
- [FFmpeg](https://ffmpeg.org/)
- Any C compiler such as [GNU Make](https://www.gnu.org/software/make/)

## Recommendations without Docker
- Debian or Ubuntu for the backend setup. Alternatively, you can utilize Windows Subsystem for Linux (WSL) on Windows 10/11.

## Setup Using Docker
1. Clone this repository.
2. Build the Docker image:
    ```
    docker build -t webui .
    ```
3. Start the application:
    ```
    docker run -p 5000:5000 webui .
    ```
4. Access the web interface by navigating to [http://localhost:5000](http://localhost:5000) in your web browser.

## Setup Without Docker
1. Clone this repository.
2. Install required packages:
    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install -y python3 rgbds build-essential git wget
    ```
3. Install Flask using pip3:
    ```bash
    pip3 install --upgrade pip
    pip3 install Flask
    ```
4. Download FFmpeg static build:
    ```bash
    wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-4.4.1-amd64-static.tar.xz
    ```
5. Extract only ffmpeg binary:
    ```bash
    tar -xf ffmpeg-4.4.1-amd64-static.tar.xz --strip-components=1 --wildcards '*/ffmpeg'
    rm ffmpeg-4.4.1-amd64-static.tar.xz
    ```
6. Clone GBVideoPlayer2 repository:
    ```bash
    git clone https://github.com/LIJI32/GBVideoPlayer2 "${PWD}/GBVideoPlayer2"
    ```
7. Make ffmpeg executable and move ffmpeg to GBVideoPlayer2 directory:
    ```bash
    chmod +x ffmpeg
    mv ffmpeg "${PWD}/GBVideoPlayer2/"
    ```
8. Start the application:
    ```bash
    python main.py
    ```
9. Access the web interface by navigating to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.