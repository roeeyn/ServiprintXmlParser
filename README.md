# Serviprint XML Parser

This project is intended to help in how the invoices are processed. You upload a bunch of XMLs and the platform returns a CSV which contains all the condensed info of this XMLs, so it will be easier to read.

See the live project [here](https://serviprint-xml-parser.herokuapp.com/)

![Sample Gif](https://media.giphy.com/media/vpd79Y5fcxQivinMm5/giphy.gif)

## Project Setup

### Create a Virtual Environment

For installing the dependencies you need to first `create a virtual environment`

```shell
python -m venv xml-parser
```

### Activate the Virtual Environment

Then you need to activate your recently created virtual environment

```shell
# For Macos/Linux
source ./venv/bin/activate

# For Windows
./venv/bin/activate.bat
```

### Installing Dependencies

Install the dependencies

```shell
pip install -r requirements.txt
```

## Playground for XML extraction

For playing around with how should we do the XML extraction we created a Jupyter Lab which provided me with a quick feedback loop about how to proceed. If you want to see this notebook, you can setup a temporary Jupyter container with Docker.

```shell
docker run --rm -p 8888:8888 -v $(pwd):/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes jupyter/scipy-notebook
```
