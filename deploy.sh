echo "Building api image..."
echo "docker build -t vantoan11/codetogive2022-api:$SHA -f ./server/Dockerfile ./server"
docker build -t vantoan11/codetogive2022-api:$SHA -f ./server/Dockerfile ./server
echo "Pushing api image into docker hub..."
docker push vantoan11/codetogive2022-api:$SHA
kubectl apply -f kubernetes
kubectl set image deployments/api-deployment api=vantoan11/codetogive2022-api:$SHA