.PHONY: start stop deploy

start:
	docker-compose up -d

stop:
	docker-compose down

deploy:
	@echo "Deploying services..."
	docker-compose up -d --build
