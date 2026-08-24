# Homework 02: Tooling Setup

In this assignment I scaffolded a reproducible project structure with folders for data, code, notebooks, docs, reports, and models, using placeholder files to track otherwise empty folders in Git. I set up a config helper (`src/config.py`) to load environment variables from a `.env` file rather than hardcoding secrets, and a starter Jupyter notebook (`00_project_setup.ipynb`) to verify the environment and config are working. A `.gitignore` excludes the real `.env` file from version control, and `requirements.txt` lists the packages this project depends on.
