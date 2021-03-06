Dependencies
============
We use bottle micro-framework.


     # apt-get install python-bottle

(current code works with debian-stable version of bottle)

or

    $ pip install bottle

Running
=======

    $ ./backend.py


Then hit *http://localhost:8080*

To run in debug mode (auto-reload)

    $ DEBUG=1 ./backend.py

Bottle will reload on source change, but not on template change if you're using
an old version of bottle.

You can specify listening port and address by setting `BIND_PORT` and
`BIND_ADDR` env vars, ex:

    BIND_ADDR='0.0.0.0' BIND_PORT=8081 ./backend.py

Default is to listen on `127.0.0.0`, port `8080`.

You can also pass a `URL_PREFIX='/some_folder/'` if you don't want the app to be
served at the root of the domain.

Create the DataBase
===================

    $ python backend.py createdb

Build GeoJSON files
===================

    $ python backend.py buildgeojson

Drop the database
=================

    $ rm db.sqlite3

What else ?

Email notifications
===================

Complete a `settings.ini` at the root folder. It looks like this:

```ini
[email]
from = from@rst.org
to = you@you.org
smtp_host = mail.server.org
smtp_user = email to login to the smtp host
smtp_password = password of the host
admin_url = web administration url 
```
Note that there are no brackets.

You will now receive an email when an user fills the form.


Customizing appearance
======================

Wether you like or not balloons, you may want to override some templates and/or
static files.

You can mention a `CUSTOMIZATION_DIR` as environ variable. In that dir, you can
create *assets* and *views* subdirs, containing files with the name of the
original files you want to override from default *assets* and *views*.

For example to override only *main.css* and *base.tpl*, you would set
`CUSTOMIZATION_DIR=/home/alice/my-fancy-isp-theme` and use the following directory
layout :

    /home/alice/my-fancy-isp-theme/
    ├── assets
    │   └── main.css
    └── views
        └── base.tpl
