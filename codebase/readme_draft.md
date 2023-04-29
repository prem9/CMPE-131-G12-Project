To run this application run main.py
    If issues arise, run:
        __init__.py
        auth.py
        models.py
        views.py
    before running main.py

Explanation:
    __init__.py
        Makes the website folder a python package meaning we can import the website package and whatever is inside __init__.py is ran automatically
    auth.py
    models.py
        Used for database models
    views.py
        Stores main views aka url end points for the front-end of the website

Technology used:
    Flask
        Python framework allowing us to build simple websites
    Flask-sqlalchemy
        SQL toolkit for python allowing us to interact with databases
        Can use high-level objects instead of writing SQL queries directly
    Jinja
        A templating engine that generates HTML templates that are then rendered by the web server and sent to the client's broswer
    