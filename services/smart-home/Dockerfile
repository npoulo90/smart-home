FROM homeassistant/home-assistant:latest

WORKDIR /smart-home/app

COPY ../infra/central_requirements.txt /smart-home/app/central_requirements.txt
RUN pip install --no-cache-dir -r central_requirements.txt

VOLUME /config
EXPOSE 8123

CMD ["hass", "--config", "/config"]

RUN echo "Home Assistant Successfully Installed"
