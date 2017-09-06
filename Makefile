build:
	docker build -t mijara/adn3 .

push:
	docker push mijara/adn3

redeploy:
	make build
	make push
	ssh root@200.1.16.121 "./redeploy"

