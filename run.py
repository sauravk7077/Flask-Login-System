from login_system import createApp
from colorama import init
from flask import url_for


init()
app = createApp()
app.run()

