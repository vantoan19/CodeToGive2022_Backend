#!/bin/bash
echo "Building api image..."
docker build -t vantoan11/codetogive2022-api:$SHA -f ./server/Dockerfile ./server
docker tag
echo "Pushing api image into docker hub..."
docker push vantoan11/codetogive2022-api:$SHA
kubectl apply -f kubernetes
kubectl set image deployment/api-deployment api=vantoan11/codetogive2022-api:$SHA