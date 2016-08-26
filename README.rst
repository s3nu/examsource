ExamSource
==============================

Online exam test bank

Basic Commands
--------------
* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

Test coverage
^^^^^^^^^^^^^
To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Deployment
----------
Heroku
^^^^^^

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
