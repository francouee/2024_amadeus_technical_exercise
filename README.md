# Technical exercise Amadeus

For better clarity, the exercise is delivered in the form of a [jupyter book](https://jupyterbook.org/en/stable/intro.html) which content is located in the `docs/jupyter_book` folder.

The book contains 3 parts :
* Introduction : Place some useful context for the exercise
* EDA (Exploratory data analysis) : Show what exploratory analysis was made for the provided dataset
* Questions : The answer to the 3 questions

## Environment installation

```bash
(.venv) foo@bar~$ python3.11 -m pip install poetry # optional
(.venv) foo@bar~$ python3.11 -m poetry install
```


## Build Jupyter book

```bash
(.venv) foo@bar~$ jupyter-book build --all docs/jupyter_book 
```

* The jupyter book is available online at this url : https://francouee.github.io/2024_amadeus_technical_exercise/intro.html.
* The exercise can be run in the [docs/jupyter_book/questions.ipynb](docs/jupyter_book/questions.ipynb) notebook.