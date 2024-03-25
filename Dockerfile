# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN apt-get update && apt-get install -y \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsdl1.2-dev \
    libsmpeg-dev \
    python3-dev \
    python3-numpy \
    subversion \
    libportmidi-dev \
    ffmpeg \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    && pip install pygame \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose the port the app runs on
EXPOSE 5000

# Run the game.py script when the container launches
CMD ["python", "game.py"]
