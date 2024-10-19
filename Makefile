REGISTRY=localhost:5001
IMAGE_NAME=telegram-contribution-bot
TAG=latest

.PHONY: build push restart deploy

build:
	docker build -t $(REGISTRY)/$(IMAGE_NAME):$(TAG) .

push: build
	docker push $(REGISTRY)/$(IMAGE_NAME):$(TAG)

restart:
	kubectl rollout restart deployment $(IMAGE_NAME)

deploy: push restart
