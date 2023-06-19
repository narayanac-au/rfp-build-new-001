
FROM python:3.9-slim-buster
# FROM python3.9-nodejs16-slim

# install nginx
# RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# RUN apt-get install -y nodejs
# RUN Node --version
# COPY nginx/nginx.conf /etc/nginx/sites-available/default
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#     && ln -sf /dev/stderr /var/log/nginx/error.log

# setting working directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/app"
# prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
# copy source and install dependencies

# RUN mkdir -p /opt/app
# RUN mkdir -p /opt/app/pip_cache
# RUN mkdir -p /opt/app/dir

COPY requirements.txt start-server.sh /usr/src/app/
# COPY .pip_cache /opt/app/pip_cache/
COPY . /usr/src/app/
# WORKDIR /opt/app
# install python/system level dependencies

# RUN apt-get update && apt-get install -y libpq-dev gcc
RUN apt-get update && apt-get install -y libpq-dev gcc && \
/usr/local/bin/python -m pip install --upgrade pip==21.1.3 && \
pip install pip-tools && \
pip install --no-cache-dir -r /usr/src/app/requirements.txt

# RUN /usr/local/bin/python -c 'from sentence-transformers import SentenceTransformer; embedder = SentenceTransformer("bert-base-uncased")'

RUN apt-get install -y curl

# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | -E bash - && \
# apt-get install -y nodejs
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
 apt-get install -y nodejs

RUN npm install -g npm@6.14.13
RUN npm set audit false && npm install docx-merger

# # | -E bash -

# RUN apt-get install -y nodejs
# # # copy remaining project over

# RUN apt-get install xz-utils
# RUN apt-get -y install curl

# # Download latest nodejs binary
# RUN curl https://nodejs.org/dist/v14.15.4/node-v14.15.4-linux-x64.tar.xz -O

# # Extract & install
# RUN tar -xf node-v14.15.4-linux-x64.tar.xz
# RUN ln -s /node-v14.15.4-linux-x64/bin/node /usr/local/bin/node
# RUN ln -s /node-v14.15.4-linux-x64/bin/npm /usr/local/bin/npm
# RUN ln -s /node-v14.15.4-linux-x64/bin/npx /usr/local/bin/npx


COPY . /usr/src/app
# # create permissions for newly built image

# # create user and assign owner of logs to user

RUN sed -i -e 's/^root::/root:!:/' /etc/shadow && \
 chmod -R ugo+rw /usr/src/app/ && \
 useradd -s /bin/bash user && \
 chown user: /usr/src/app/ && \
 adduser user www-data

# switch to user
USER user

# give user write
RUN chmod u+w /usr/src/app/

# RUN chown -R www-data:www-data /usr/src/app

# # expose port that docker will map to
EXPOSE 8000
# STOPSIGNAL SIGTERM
# CMD ["/usr/src/app/start-server.sh"]


# RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
# RUN chown -R www-data:www-data /opt/app

# # start server
# EXPOSE 8000
# STOPSIGNAL SIGTERM
# CMD ["/opt/app/start-server.sh"]