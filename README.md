# Data Mesh Project
This project focus on the study of the Data Mesh. The architecture of the solution applied in this project is based on my interpretation of the book [Data Mesh - Delivering Data-Driven Value at Scale by Zhamak Dehghani](https://www.booktopia.com.au/data-mesh-zhamak-dehghani/book/9781492092391.html?source=pla&gclid=Cj0KCQjw1N2TBhCOARIsAGVHQc7aSFNn--n-S1Z3I4MLhRe3rUcwiGUFwIkC84y-_rPZ2BNXF6B2-AEaAvcjEALw_wcB).

### Stack

We use the following technologies:

1. Snowflake
1. Pulumi
1. Python with FastAPI among other libraries. We provide more details about each one of them and their use as we move on with the project.

### Setting up the dev environment

Pre-requisites:

1. [VS Code IDE](https://code.visualstudio.com/download)
1. [Docker Extension for VS Code](https://code.visualstudio.com/docs/containers/overview)
1. [Remote Explorer Extension] [comment]: <> (#TODO: add a link)
1. [Remote Development Extension] [comment]: <> (#TODO: add a link)
1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
1. [Register on Docker Hub](https://hub.docker.com/)

OBS: This tutorial will cover the setup process using VS code but if you have preferecer for another IDE feel free to use and adapt the steps for your tool.

Step-by-step Installation:

1. Open `Docker Desktop`, and make sure the Docker whale on the left bottom corner is green. [comment]: <> (#TODO: add a picture)
1. Open VS code and open the terminal (click on Terminal > New Terminal). [comment]: <> (#TODO: add a picture)
1. Type the command `docker --version` and then hit `enter`. You should have a result like `Docker version 20.10.21, build baeda1f`. It means your Docker is working fine.
1. Type `docker pull rvasconcelossilva/data-mesh-tool` and then hit `enter`. You will be able to see the image `rvasconcelossilva/data-mesh-tool` in the `Docker Desktop`.
1. Back to VS Code, type `docker run --name dev -p 8000:80 rvasconcelossilva/data-mesh-tool`, it will create the container so you can contribute to the `data-mesh` project.
1. On VS Code, click on the left bottom corner, and select the option `Attach to Running Container...`, and the click on `/dev`. A new VS Code will pop up and the project will load.
1. Click again in Terminal, and then new terminal.
1. Open the brownser and access `http://0.0.0.0:8000/`
1. Back to the terminal, type `cd /code/data-mesh && zsh`.

Done! You are good to go.




[Markdown Documentation](https://www.markdownguide.org/getting-started/)\

docker pull rvasconcelossilva/data-mesh-tool
