FROM homeassistant/home-assistant:latest

WORKDIR /smart-home/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


VOLUME /config
EXPOSE 8123

CMD ["hass", "--config", "/config"]

RUN echo "Home Assistant Successfully Installed"

