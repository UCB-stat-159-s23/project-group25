# This makefile creates conda environment and ipykernel for the environment

# Name of the conda environment
CONDA_ENV_NAME = project-group25`

# Create the conda environment from the environment.yml file
create-environment:
    conda env create -n $(CONDA_ENV_NAME) -f environment.yml

# Add the ipykernel to the conda environment
add-ipykernel:
    conda activate $(CONDA_ENV_NAME)
    pip install ipykernel
    python -m ipykernel install --user --name $(CONDA_ENV_NAME) --display-name "$(CONDA_ENV_NAME)"
    conda deactivate