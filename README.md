# fake_insta
Instagram clone for study

# Setting up a virtual env
pip install virtualenv \
virtualenv <Name_of_the_env>

# Activate the virtual environment
You can activate the python environment by running the following command:

## Mac OS / Linux:
source mypython/bin/activate
## Windows
mypthon\Scripts\activate

## smtp server
(venv) $ python -m smtpd -n -c DebuggingServer localhost:1025

Start a simple smtp server to view messages related to password reset emails
in the terminal.

# Project requirements
### Docker-Compose

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version