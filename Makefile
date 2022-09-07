minikube:
	minikube start

build-dev:
	docker build --tag server:latest .

dev:
	chmod +x dev.sh
	sh dev.sh