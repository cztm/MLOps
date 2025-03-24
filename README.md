## Overview
#This repository contains the setup scaffolding for course labs and a class project related to MLOps. It demonstrates best practices for structuring a development environment. 

## Environment Setup
#This lab uses **VS Code** as the development environment and sets up a **conda environment** with dependencies specified in `environment.yml`.

### Steps Included:
1. Create and activate a conda environment:
    ```bash
    conda create --name mlops python=3.12
    conda activate mlops
    ```
2. Install packages from `environment.yml`:
    ```bash
    conda env update --file environment.yml --prune
    ```
##  Project Structure
mlops/
|--data/
|--notebooks/
|--models/
|--labs/
   |--labs1-10/
|--environment.yml
|--README.md
|__.gitignore

