# About This Image
This image hosts a juypter notebook server for *single users* to run workloads on a *cpu*. This image doesn't support *gpus*. The image is automatically updated with the latest python datascience packages.

# How to use this image
Sample command to run on linux:  
`sudo docker run -d --name datascience --restart unless-stopped -p 8888:8888 -v ~/datsci:/work --network="host" skark/datascience`

Sample command to run on Windows:  
`docker run -it --rm --name datascience -p 8888:8888 -v C:\datascience:/work skark/datascience`

Connect the running container using `http://localhost:8888/`
