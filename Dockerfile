# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.6-alpine


EXPOSE 8865

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

ENV C_FORCE_ROOT true

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Making source and static directory
RUN mkdir /src
RUN mkdir /static
WORKDIR /src

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg \
    openblas \ 
    libstdc++ 

# Installing temporary packages required for installing requirements.pip 
RUN apk add --no-cache --virtual build-deps \
    gcc \  
    python3-dev \ 
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev \
    g++ \
    openblas-dev \
    cmake \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h

# Update pip
RUN pip install --upgrade pip


# Installing scipy
RUN pip install --no-cache-dir --disable-pip-version-check scipy==1.3.1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /src


# removing temporary packages from docker and removing cache 
RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip
# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN useradd appuser && chown -R appuser /app
#USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'PelicarusWS'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8865", "PelicarusDJWS\wsgi.py"]
