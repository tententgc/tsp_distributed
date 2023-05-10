# Use the official Python image as a base
FROM python:3.9-slim

# Install the Concorde TSP Solver
RUN apt-get update && apt-get install -y \
    build-essential \
    libgmp-dev \
    libmpfr-dev \
    libmpc-dev \
    wget

RUN wget http://www.math.uwaterloo.ca/tsp/concorde/downloads/codes/src/co031219.tgz && \
    tar xf co031219.tgz && \
    cd concorde && \
    CFLAGS='-O3 -march=native -mtune=native -fPIC' ./configure && \
    make && \
    cp -r . /usr/local && \
    cd .. && rm -rf concorde

RUN pip install --no-cache-dir pyconcorde

# Set the working directory
WORKDIR /app

# Copy the required files
COPY master.py worker.py ./

# Expose the port the app runs on
EXPOSE 5010

# Start the application
CMD ["python", "master.py"]
