
FROM python:3.9-slim-buster

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

RUN apt-get update && apt-get install -y libpq-dev gcc && \
/usr/local/bin/python -m pip install --upgrade pip==21.1.3 && \
pip install pip-tools && \
pip install --no-cache-dir -r /usr/src/app/requirements.txt

# # copy remaining project over

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
STOPSIGNAL SIGTERM
# CMD ["/usr/src/app/start-server.sh"]


# RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
# RUN chown -R www-data:www-data /opt/app

# # start server
# EXPOSE 8000
# STOPSIGNAL SIGTERM
# CMD ["/opt/app/start-server.sh"]