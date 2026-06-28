import json
import os
import threading
import uuid

# import dotenv
import yaml
from flask import Flask, after_this_request, flash, render_template, request, send_file

from .file_converter import Convert

# dotenv.load_dotenv()  # For passwords

jobs = {}


class WWW:
    def __init__(self, debug: bool = False, config_file: str = "./config.yml") -> None:
        self.www = Flask(__name__)
        # self.www.secret_key = os.environ.get("SECRET_KEY") #  For passwords if you want
        self.config_file = config_file
        with open(self.config_file, "r") as data:
            self.config = yaml.safe_load(data)
        self.temp_folder = os.path.abspath(self.config["temp_folder"])
        self.www.secret_key = self.config["secret_pass"]
        os.makedirs(self.temp_folder, exist_ok=True)

        self.data = {}
        with open("client/conversions.json", "r+") as file:
            self.data = json.loads(file.read())

        self._register_routes()
        self._register_errors()
        self._register_tools()
        self.debug = debug

        if self.debug:
            self._regesiter_dev()

    def _register_routes(self) -> None:
        @self.www.route("/")
        def _index():
            return render_template("index.html")

        @self.www.route("/about")
        def _about():
            return render_template("about.html")

    def _register_tools(self):
        @self.www.route("/fileconvert", methods=["GET", "POST"])
        def _fconv():
            if request.method == "POST":
                file = request.files["file"]
                format = request.form["format"]
                category = request.form["category"]

                job_id = str(uuid.uuid4())
                temp_path = os.path.join(self.temp_folder, str(file.filename))
                file.save(temp_path)

                jobs[job_id] = {"status": "converting", "file": None}

                def run_conversion():
                    result = Convert(temp_path, format, category)
                    jobs[job_id]["file"] = result
                    jobs[job_id]["status"] = "done" if result else "error"
                    try:
                        os.remove(temp_path)
                    except Exception:
                        pass

                threading.Thread(target=run_conversion).start()
                return {"job_id": job_id}

            return render_template("tools/fileconverter.html", fileDict=self.data)

        @self.www.route("/fileconvert/status/<job_id>")
        def _fconv_status(job_id):
            job = jobs.get(job_id)
            if not job:
                return {"status": "not_found"}, 404
            return {"status": job["status"]}

        @self.www.route("/fileconvert/download/<job_id>")
        def _fconv_download(job_id):
            job = jobs.get(job_id)
            if not job or job["status"] != "done":
                return {"error": "not ready"}, 400

            return_file = job["file"]

            @after_this_request
            def cleanup(response):
                threading.Thread(
                    target=lambda: (
                        __import__("time").sleep(2),
                        os.remove(return_file),
                        jobs.pop(job_id, None),
                    )
                ).start()
                return response

            return send_file(return_file, as_attachment=True)

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
        self.www.run(**kwargs, debug=self.debug)
