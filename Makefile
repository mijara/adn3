build:
	docker build -t mijara/adn3 .

push:
	docker push mijara/adn3

all: build push

