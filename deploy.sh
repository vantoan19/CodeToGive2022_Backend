echo "Building api image..."
docker build -t vantoan11/codetogive2022-api:$SHA -t vantoan11/codetogive2022-api:latest -f ./server/Dockerfile ./server
echo "Pushing api image into docker hub..."
docker push vantoan11/codetogive2022-api:$SHA
docker push vantoan11/codetogive2022-api:latest
kubectl apply -f kubernetes
kubectl set image deployments/api-deployment api=vantoan11/codetogive2022-api:$SHA