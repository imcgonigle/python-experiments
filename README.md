# Python Experiments
This repo contains small Python programs that I've written to explore the Python programming language and different Python libraries.

## Experiments

### Basics
Basic experiments are like any other experiments but they don't have any external dependecies. You can run any of these experiments with `python experiments/basics/{EXPERIMENT_NAME}.py`

- **bulk-file-renamer.py** - Interactive CLI tool for renaming all files in a directory.
- **password-generator.py** - Interactive CLI tool for generating strong passwords.
- **task-scheduler.py** - An interactive program that allows you to schedule tasks to be run in the future.
- **folder-monitor.py** - A program that monitors a directory for changes and lists them as they happen.

### Other Experiments
To run any of these experiments, checkout out the [instructions](#running-the-experiments) below.

- **fetch-links.py** - Scrapes a webpage for links and prints them in a table.
- **gui-scrape-link.py** - A GUI program that lets you enter a URL for it to scrape and display all of the links it finds.

## Running the Experiments

All of the experiments in `experiments/basics/` have no external dependencies so they can be run with just Python installed. `python experiments/basics/{EXPERIMENT_NAME}`

All other experiments use `pipenv` to manage dependencies.

### Requirements
- Install [pyenv](https://github.com/pyenv/pyenv)
- Install [pipenv](https://pipenv.pypa.io/en/latest/installation.html)
- Install Python `pyenv install 3.12`

#### 1. Change into the experiment directory
`cd experiments/{EXPERIMENT_NAME}`

#### 2. Create a virtual environment
`pipenv shell`

#### 3. Install the dependencies
`pipenv install`

#### 4. Run one of the experiments
`pipenv run python {EXPERIMENT_NAME}`

