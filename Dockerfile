FROM andygarfield/geopandas
RUN python -m pip install flask && \
    mkdir /app
ADD . /app
WORKDIR /app
ENV FLASK_APP server.py
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "-p", "80"]
