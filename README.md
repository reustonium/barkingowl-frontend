barkingowl-frontend
===================

A very lite frontend for the barkingowl document scraping system.

### Running Locally

Getting started is easy!

First, barkingowl depends on python 2.7, you can download it [here](https://www.python.org/downloads/release/python-279/)

Then use pip to install virtualenv, a virtual environment manager for creating isolated python development environments.

```
pip install virtualenv
```

A second dependency is RabbitMQ.  You can find information about installing RabbitMQ on your
system here: [http://www.rabbitmq.com/download.html](http://www.rabbitmq.com/download.html)

Next, execute these commands to launch the server:

    $ virtualenv barkingowl-frontend-venv
    $ source barkingowl-frontend-venv/bin/activate
    $ git clone https://github.com/thequbit/barkingowl-frontend
    $ pip install barkingowl
    $ cd barkingowl-frontend
    $ python server.py

This will launch a flask-based web server on port 8067.  You can access the site by going to this url:

    http://127.0.0.1:8067/

You will see a single, simple page.  On this page there are two main functions: 1) upload a csv file to the site so it can be configured into the barkingowl dispatcher, and 2) shutdown the entire barkingowl system.


### Deploy to Heroku

1. Sign up for a free [Heroku](https://heroku.com) account
2. Download the [Heroku Toolbar](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) for your OS
3. From git bash login to heroku `heroku login`
4. Create an app on the heroku platform `heroku create`
5. Deploy BarkingOwl Frontend `git push heroku master`
This process pushes this codebase to heroku and runs the deployment process, this can take several minutes.
6. Open your deployment `heroku open`

For more information head over to the [wiki](https://github.com/thequbit/barkingowl-frontend/wiki)
