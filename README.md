# Python Experiments
This repo contains small Python programs I've written to learn more about Python and different Python libraries

## Getting Started

**Strat by cloning the repo**
`git clone https://github.com/imcgonigle/python-experiments.git`

### Basic Experiments (experiments/basics)
The basic experiments don't require any external dependecies.

#### Run one of the experiments
You can run anything in `experiments/basics` by simply running `python experiments/basics/{EXPERIMENT_NAME`

### Other Experiments
Most of the experiments have external dependencies installed with pipenv.

#### Requirements
- Install [pyenv](https://github.com/pyenv/pyenv)
- Install [pipenv](https://pipenv.pypa.io/en/latest/installation.html)

#### Create a virtual environment
`pipenv shell`

#### Install the dependencies
`pipenv install`

#### Run one of the experiments
`pipenv run python experiments/{EXPERIMENT_NAME}`

## Experiments
- fetch-links.py - Scrapes a webpage for links and prints them in a table.
- gui-scrape-link.py - A GUI program that lets you enter a URL for it to scrape and display all of the links it finds.

