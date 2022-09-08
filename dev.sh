#!/bin/bash

echo "Creating the persistent volumn claim..."
kubectl apply -f ./kubernetes/dev/postgres-persistent-volume-claim.yaml

echo "Creating database password secret..."
kubectl create secret generic postgres-password --from-literal=POSTGRES_PASSWORD=codetogive_2022

echo "Creating Postgres deployment and ip service..."
kubectl apply -f ./kubernetes/dev/postgres-deployment.yaml
kubectl apply -f ./kubernetes/dev/postgres-cluster-ip-service.yaml

echo "Creating Redis deployment and ip service..."
kubectl apply -f ./kubernetes/dev/redis-deployment.yaml
kubectl apply -f ./kubernetes/dev/redis-cluster-ip-service.yaml

echo "Creating server deployment and ip service..."
kubectl apply -f ./kubernetes/dev/server-deployment.yaml
kubectl apply -f ./kubernetes/dev/server-cluster-ip-service.yaml

echo "Setting ingress and ingress service..."
minikube addons enable ingress
kubectl apply -f ./kubernetes/dev/ingress-service.yaml