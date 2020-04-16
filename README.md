# About This Image
This image hosts a juypter lab server for **single users** to run workloads on **CPUs**. This is ideal for systems without a dedicated gpu. The image is automatically updated with the latest python datascience libraries like pytorch, tensorflow, scikit-learn etc.

# How to use this image
Sample command to run on linux:  
`sudo docker run -d --name datascience --restart unless-stopped -p 8888:8888 -v ~/datsci:/work --network="host" skark/datascience`

Sample command to run on Windows:  
`docker run -it --rm --name datascience -p 8888:8888 -v C:\datascience:/work skark/datascience`

Connect to the running container using `http://localhost:8888/`
