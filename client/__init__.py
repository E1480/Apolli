import os

import dotenv
from flask import Flask, flash, render_template, request

dotenv.load_dotenv()


class WWW:
    def __init__(self, debug: bool = False) -> None:
        self.www = Flask(__name__)
        self.www.secret_key = os.environ.get("SECRET_KEY")
        self._register_routes()
        self._register_errors()

        if debug:
            self._regesiter_dev()

    def _register_routes(self) -> None:
        @self.www.route("/")
        def _index():
            return render_template("index.html")

        @self.www.route("/about")
        def _about():
            return "About"

    def _regesiter_dev(self) -> None:
        @self.www.route("/doc")
        def _doc():
            from flask import flash

            flash("Saved successfully!", "success")
            flash("Something went wrong.", "error")
            return render_template("_doc.html")

    def _register_errors(self) -> None:
        @self.www.errorhandler(404)
        def _404(e):
            flash("Error 404", "error")
            attempt_url = request.path.removeprefix("/")
            return (
                render_template("errors/404.html", link=attempt_url),
                404,
            )

    def run(self, **kwargs):
        self.www.run(**kwargs)
