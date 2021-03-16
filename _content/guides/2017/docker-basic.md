# Basic Usage for Docker
- date: 2017-11-06 16:12
- tags: linux, docker
- category: guides
-------

Just to keep some notes when started to use docker for my development projects.

### 0. Get Started

For my mac, download the .dmg file from official web site. Then it will run a program with a task icon in the top bar.

After the program has been initialized, you can open a terminal and try a few commands:

```bash

# check versions
$ docker --version
$ docker-compose --version
$ docker-machine --version

# Current images
$ docker images

# Running instances
$ docker ps

```

### 1. First Instance

The docker official Hello World image is small enough, which you can try as your first instance.

```bash

$ docker run hello-world

```

The image does not exist locally currently, but docker will continue to try downloading it and then run it.

Then, you wil see the image locally.

```bash

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              725dcfab7d63        2 days ago          1.84kB

```

However, the container for this image is not visible in the list because **the process has existed**. You need to use a `-a` parameter to see it:

```bash

$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
c32eac048fda        hello-world         "/hello"            5 minutes ago       Exited (0) 5 minutes ago                       cranky_shaw

```

### 2. Server Instance

The Hello World container doesn't do anything. If you want to try something interesting, try the [nginx image](https://docs.docker.com/docker-for-mac/#explore-the-application-and-run-examples) instead.

```bash

$ docker run -d -p 8001:80 --name webserver1 nginx

```

I choose a different port for the server, just to show how the port mapping is handled. When you check the instance with `docker ps`, you can see the image name, instance name, and the port mapping and get the meaning. When the container is up, you can access `http://localhost:8001/` to see the nginx home page.

```bash

$ docker ps 
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                  NAMES
6f6ba1d3f285        nginx               "nginx -g 'daemon ..."   About a minute ago   Up About a minute   0.0.0.0:8001->80/tcp   webserver1

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nginx               latest              40960efd7b8f        38 hours ago        108MB
hello-world         latest              725dcfab7d63        2 days ago          1.84kB

```

A good point is that you can see how much disk usage every image uses. Now you can stop the service, or remove the unused resources by commands.

```bash

# container life cycle methods
$ docker stop webserver1
$ docker start webserver1
$ docker restart webserver1


# remove a container
$ docker rm webserver1

# remove an image
$ docker rmi hello-world

```

For server instance like Ubuntu, you need an interactive shell to work with it, so the command will be a little bit different:

```
# start a new container named 'ubuntu'
$ docker run --name ubuntu -ti ubuntu-core

# run an existing container
$ docker container start -i ubuntu

# attach console to a server if it has started without interactive environment
$ docker container start ubuntu
$ docker attach ubuntu

# If you want to detach from a server without stopping it
# use `ctrl-p ctrl-q` key sequence

```

You may wonder the file size of each containers, you can checkt it by `docker ps -s`. You can see a ubuntu core only uses very small space with the minimal setup.

```bash

$ docker ps -s
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES               SIZE
070a6e845653        ubuntu              "/bin/bash"              About an hour ago   Up About an hour                           ubuntu              96.7MB (virtual 219MB)
0200f61f5d65        nginx               "nginx -g 'daemon ..."   2 hours ago         Up 2 hours          0.0.0.0:5000->80/tcp   webserver           2B (virtual 108MB)

```

### 3. Other Settings

There are some Docker preferences also mentioned in the Get Started guide, which I should make some notes here:

 * **Disk Image Location**. on Mac, it is stored in a file called "Docker.qcow2" somewhere in ~/Library, and all the containers are store within this image. You can move it somewhere else.
 * **Experimental features**. It is not recommended for production environment, then I wonder why it is turned on by default on Mac.
 * **Registry, Configuration, and Certificates for the Daemon **, use it when you needed.
 
#### 3.1 Download Images by Tags

```bash
# Download images/repos from registry
$ docker pull <image>:<tag>

# Example of getting a core ubuntu system
$ docker pull ubuntu:xenial
$ docker run --name ubuntu -ti ubuntu

```



### 4. Docker for Mac vs Docker Toolbox

Docker Toolbox is also installed by the .dmg installation. The programs include `docker-compose` and `docker-machine`.

 * Docker for Mac is a Mac native  application, you get only one VM, and it is managed by Docker for Mac. The VM is used with a lightweight solution called HyperKit.
 * Using Dokcker Toolbox, you can set up one or more VM and manage them.


### 5. Docker Architecture

The Docker architecture can split into 3 parts:

 * Docket Client, the `docker` cli tools for user to interact with docker daemon with Docker API.
 * Docker Host, the service daemon `dockerd` listen for Docker API request and perform all kinds of management tasks about images, containers, networks, and volumns.
 * Docker Registry, a cloud service which stores Docker images, such as Docker Hub and Docker Cloud(both are public registries).


#### 5.1 Docker Objects

 * Image, a read-only template with instructions for creating Docker container.
 * Container, an instance of an image, with network, file system, etc. attached. You can create, delete, stop, resume containers.
 * Service, allow you to scale containers across Docker daemons.

#### 5.2 The Underlying technology

 * Namespaces. When you run a container, Docker create a set of namespaces for the container, which provide a layer of isolation. The namespaces includes:
    * `pid` for process
    * `net` for network interfaces
    * `ipc` for interprocess communication
    * `mnt` for file system
    * `uts` for kernel and version identifiers (Unix Timeshare System)
 * Control Groups. A `cgroup` limits an application to a specific set of resources, and allow Docker Engine to share hardware resources to containers with optionally limits and constraints.
 * Container Format. A combination of namespaces, control groups, and UnionFS, packed into a Wrapper. The default format is `libcontainer`.


Refs:
[Docker Architecture](https://docs.docker.com/engine/docker-overview/#docker-architecture)
[Docker Store](https://store.docker.com/) is a market where you can distribute your images.

### 6. Developing Apps with Docker

It's easy to setup Docker to deploy with your app. All you need to do is to add a `Dockerfile` in your source folder and then build the image. The official example demonstrate how a small flask app is built with Docker.

#### 6.1 First time image

I summarize the steps as below:

 * Go to docker [hub](https://hub.docker.com/_/python/) to find a target python image. It already has all kinds of  Dockerfile template for you to copy.
 * Create a local copy of the Docker file. Make sure you understand the template and knows what to modify according to your app.
 * Write a flask `app.py` and a `requirements.txt` as usual.
 * Build the docker image and then run with it.

```bash
# prepare the source files(...skipped here)
$ ls
Dockerfile    app.py      requirements.txt

# build the image
$ docker build -t slim-flask .

# create and run the container
$ docker run -p 4000:80 slim-flask
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)

```

The result will be:

 * Only a Dockerfile is added to your source, and others are still remain
 * A Python docker image is downloaded, which takes the size of 156MB or 691MB depends on if you choose the "slim" version.
 * A flask image for your app is genenrated, which contains the content from the original python image, the pip installed packages from requirements, and your source files. So the size is slightly bigger than the python image.

```bash

$ docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
slim-flask          latest              3032f935f40c        10 seconds ago      166MB
python              slim                a79297999298        45 hours ago        156MB

```

#### 6.2 Create image from a container

However, sometimes you want to make configurations inside a container and want to save it as an image. You can do that:

```bash

$ docker container commit [options] CONTAINER [repository:[TAG]]

# example
$ docker container commit ubuntu ubuntu-image

```

#### 6.3 Publish docker image

Use it when it is needed.

```bash
$ docker login             # Log in this CLI session using your Docker credentials
$ docker tag <image> username/repository:tag  # Tag <image> for upload to registry
$ docker push username/repository:tag            # Upload tagged image to registry
$ docker run username/repository:tag                   # Run image from a registry
```

### 7. Docker mirrors

* Docker(Official), `--registry-mirror=https://registry.docker-cn.com`
* Netease, http://hub-mirror.c.163.com
* USTC, https://docker.mirrors.ustc.edu.cn
* Daocloud & Alicloud, need registration, and Alicloud needs an dev platform account.

[source](https://ieevee.com/tech/2016/09/28/docker-mirror.html)



