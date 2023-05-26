###########
# BUILDER #
###########

# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

# lint
RUN pip install --upgrade pip
# RUN pip install flake8==3.9.2
COPY . .
# RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
RUN apt-get update && apt-get install -y libpq-dev gcc && \
    /usr/local/bin/python -m pip install --upgrade pip==21.1.3 && \
    pip install pip-tools && \
    pip install --no-cache-dir -r /usr/src/app/requirements.txt


# #########
# # FINAL #
# #########

# # pull official base image
# FROM python:3.9.6-alpine

# # create directory for the app user
# RUN mkdir -p /home/app

# # create the app user
# RUN addgroup -S app && adduser -S app -G app

# # create the appropriate directories
# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/staticfiles
# RUN mkdir $APP_HOME/mediafiles
# WORKDIR $APP_HOME

# # install dependencies
# RUN apk update && apk add libpq
# COPY --from=builder /usr/src/app/wheels /wheels
# COPY --from=builder /usr/src/app/requirements.txt .
# RUN pip install --no-cache /wheels/*


# # copy entrypoint.prod.sh
# # COPY ./entrypoint.prod.sh .
# # RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
# # RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# # copy project
# COPY . $APP_HOME

# # chown all the files to the app user
# RUN chown -R app:app $APP_HOME

# # change to the app user
# USER app

# # run entrypoint.prod.sh
# # ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]


# # Dockerfile

# FROM python:3.9-buster

# # install nginx
# RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# COPY nginx.default /etc/nginx/sites-available/default
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#     && ln -sf /dev/stderr /var/log/nginx/error.log

# # copy source and install dependencies
# RUN mkdir -p /opt/app
# RUN mkdir -p /opt/app/pip_cache
# RUN mkdir -p /opt/app/rfp_app
# COPY requirements.txt start-server.sh /opt/app/
# COPY .pip_cache /opt/app/pip_cache/
# COPY . /opt/app/rfp_app/
# WORKDIR /opt/app
# RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
# RUN chown -R www-data:www-data /opt/app

# # start server
# EXPOSE 8020
# STOPSIGNAL SIGTERM
# CMD ["/opt/app/rfp/start-server.sh"]