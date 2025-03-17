#!/usr/bin/env python3
""" create simple route """


from flask import Flask, request, render_template
from os import getenv

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Get simple route and return html
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)