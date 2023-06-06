#!/bin/sh

uwsgi --socket=0.0.0.0:8000 \
      --module=KPM.wsgi:application \
      --master \
      --max-requests=5000 \
      --buffer-size=32768 \
      --harakiri=20 \
      --processes=4 \
      --socket-timeout=300 \
      --single-interpreter \
      --enable-threads \
      --log-master