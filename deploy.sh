echo "Building api image..."
docker build -t vantoan11/codetogive2022-api:$SHA -t vantoan11/codetogive2022-api:latest -f ./server/Dockerfile ./server
docker build -t vantoan11/codetogive2022-client:$SHA -t vantoan11/codetogive2022-client:latest -f ./client/Dockerfile ./client
echo "Pushing api image into docker hub..."
docker push vantoan11/codetogive2022-api:$SHA
docker push vantoan11/codetogive2022-api:latest
docker push vantoan11/codetogive2022-client:$SHA
docker push vantoan11/codetogive2022-client:latest
kubectl apply -f kubernetes
kubectl set image deployments/api-deployment api=vantoan11/codetogive2022-api:$SHA
kubectl set image deployments/client-deployment api=vantoan11/codetogive2022-client:$SHA