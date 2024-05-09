deploy and ensure to set the port in your docker
invoke the service by calling: http://[IP of your host machine]:[PORT that you have setup]/battery_status?username=[username]&password=[password]

build image with: docker build --platform=linux/amd64 -t fusion-solar-api .
