django-sample
=============

django app

Get started
-----------



For developing at local on cross-platform, using `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_ is recommended.

setup dev environment by command:

::

  $ cd <project path>
  $ mkvirtualenv -a . -r requirements/local.txt -p python3 <venv name>

Make sure application configured with proper values in env files . env files located in according application environments:
::

 $ <project path>/.envs/(local|product|test)


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy apps

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest


Celery
^^^^^^

This app comes with Celery.

Make sure Selery is installed properly.

To run a celery worker:

.. code-block:: bash

    cd auth_service
    celery -A apps.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/ or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



Docker (Unavailable)
^^^^^^^^^^^^^^^^^^^^


