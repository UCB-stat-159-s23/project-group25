# by default, each line in the markfile will run in a different shell. 
# The .ONESHELL: command allow us to run all the commands inside an operation in the same shell. 
.ONESHELL:
SHELL = /bin/bash

# Name of the conda environment
CONDA_ENV_NAME = diabetes_analysis

# install the environment
.PHONY: env
env:
	source /srv/conda/etc/profile.d/conda.sh # configure shell to use 'conda activate'. 
	conda env create -f environment.yml -p ~/envs/$(CONDA_ENV_NAME)
	conda activate $(CONDA_ENV_NAME)
	python -m ipykernel install --user --name $(CONDA_ENV_NAME) --display-name "$(CONDA_ENV_NAME)"

# run all the notebooks
.PHONY: all
all: 
	jupyter execute codes/EDA.ipynb --kernel_name=$(CONDA_ENV_NAME)   
	jupyter execute codes/main.ipynb --kernel_name=$(CONDA_ENV_NAME)

# remove the environment
.PHONY: remove-env
remove-env:
	conda deactivate 
	mamba env remove -n $(CONDA_ENV_NAME)

# update the environment
.PHONY: update-env
update-env:
	mamba env update --file environment.yml --prune
	conda activate $(CONDA_ENV_NAME)
	python -m ipykernel install --user --name $(CONDA_ENV_NAME) --display-name "$(CONDA_ENV_NAME)"
    
# build the JupyterBook normally
.PHONY: html
html:
	jupyter-book build .

## - html-hub: build static website so it can be viewed on hosted JupyterHub (via URL proxy).
.PHONY: html-hub
html-hub: conf.py
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}proxy/absolute/8000
	@echo
	@echo "To start the Python http server, use:"
	@echo "python -m http.server --directory ${PWD}/_build/html"
	@echo "and visit this link with your browser:"
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"

# clean up the generated figures, tables and _build folders.
.PHONY: clean
clean:
	rm -rf figures/* _build/* 
	cd figures && touch .gitkeep   

