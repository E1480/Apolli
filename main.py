from client import WWW

if __name__ == "__main__":
    app = WWW(True)
    app.run(host="0.0.0.0", port=8080, debug=True)
