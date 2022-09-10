#!/bin/bash

echo "Building api image..."
docker build -t vantoan11/codetogive2022_api:latest -t vantoan11/codetogive2022_api:$SHA ./server

echo "Pushing api image into docker hub..."
docker push vantoan11/codetogive2022_api:$SHA
docker push vantoan11/codetogive2022_api:latest

kubectl apply -f kubernetes
kubectl set image deployment/api-deployment api=vantoan11/codetogive2022_api:$SHA