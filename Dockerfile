# For more information, please refer to https://aka.ms/vscode-docker-python
FROM debian:stretch-slim

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev python3.5 libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3
RUN apt-get -y install python3-numpy
RUN apt-get -y install python3-matplotlib
RUN apt-get -y install python3-scipy
RUN apt-get -y install python3-numexpr
RUN apt-get -y install python3-tables
RUN apt-get -y install python3-bs4
RUN apt-get -y install python3-html5lib
RUN apt-get -y install python3-lxml


# Update pip
RUN pip3 install --upgrade pip

# Install pip requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt


EXPOSE 8865

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

ENV C_FORCE_ROOT true

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Making source and static directory
COPY . /src
RUN mkdir /static
WORKDIR /src
# cleaning up unused files
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && rm -rf /var/lib/apt/lists/*

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN useradd appuser && chown -R appuser /app
#USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'PelicarusWS'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8865", "PelicarusDJWS\wsgi.py"]
