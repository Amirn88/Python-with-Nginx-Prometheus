# Python-with-Nginx-Prometheus
Python-with-Nginx-Montring with Prometheus

Dockerfiles Python, Nginx
Helm-Chart
Deploy into K8S
Prometheus for Montring Python and Nginx 

nginx.conf
server {
    listen 80;

    location / {
        proxy_pass http://hostname:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

-----------------------------------------------------------------
#docker network create my-network
------------------------------------------------------------------
Dockerfile-Python-file/#docker build -t my-python .
 
#docker run -d --name python-app --hostname py-app --network my-network  -p 8000:8000 my-python


Dokerfile-Nginx-file/#docker build -t my-Nginx .

#docker run -d --name ngnix-app --network my-network --hostname web-app -p 80:80 my-nginx
