# django-demo
Django 2.0 demo website

## Description
Simple Django web application built with PyEnv based on:
[Build your first website with Python and Django](https://djangobook.com/build-first-website-python-django/)

## Setup
PyEnv was used to select the proper Python version to be used along with
VirtualEnv as well as Git for source control.

Django 2.0.6 version is used with the Django Debug Toolbar.

Python Anywhere is used for demo deployment, the instructions herein assume
that.

## Installation
Please follow the next recommended sequence of instructions to install and
deploy:

### PyEnv
Copy and paste the following in the console/terminal:

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

### Update .bashrc
Edit your .bashrc file and add the following at the end of the file:

    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

To continue, refresh/rehash the shell.

### Install Python 3.6.3
Install in case this particular version is not readily available; otherwise,
skip to the next section:

    pyenv install 3.6.3

Verify the installation went through:

    pyenv versions

You should see something like this after executing the previous command:

    * system (set by /home/fbenavides69/.pyenv/version)
    3.6.3

Now prepare the virtual environment with the given Python version, within the
local source code repository:

    pyenv virtualenv 3.6.3 django206_python363
    pyenv activate django206_python363

### Clone the sources from Github
Copy and paste the following in the console/terminal:

    git clone https://github.com/fbenavides69/django-demo.git

    cd django-demo
    pip install -r requirements.txt
    pip install mysqlclient


### Run the server





