build-dev:
	docker build --tag server:latest .

minikube:
	minikube start

dev:
	chmod +x dev.sh
	sh dev.sh