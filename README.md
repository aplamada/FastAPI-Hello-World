# FastAPI Hello World

Similar to [FastAPI Hello World](https://renkulab.io/projects/andrei.plamada/fastapi-hello-world).

The aim of the project is to check the feasibility of using RenkuLab to create web servers that can be publically used (as long the session is running).

`main.py` corresponds to the example from [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/#fastapi-in-containers-docker) and it contains two endpoints:

- `/` returning `{"message": "Hello World"}`
- `/items/{item_id}` with `q` a potential query parameter and it should return `{"item_id": item_id, "q": q}`

The repo is a default one with only several changes inspired from [How to deploy Streamlit in renku](https://renku.discourse.group/t/how-to-deploy-streamlit-in-renku/169):

- install FastApi and Uvicorn in `requirements.txt`
- tell jupyter to start uvicorn in `jupyter_notebook_config.py`
- update the `default_url` in `.renku/renku.ini` to use the FastAPI root endpoint.
