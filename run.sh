echo "stop frontend"
docker stop frontend
docker rm frontend

echo "build $1"
docker build -t $1 .
docker run -d --name frontend -p 7860:7860 $1
