#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server
from testeapp import app

manager = Manager(app)
manager.add.command("runserver", Server())
manager.add.command("shell", Shell())
manager.run()
