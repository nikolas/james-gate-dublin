from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
<!doctype html>
<html>
<head>
<title>Lennart Poettering's cool shop!</title>
<style type="text/css">
body {
    background: purple;
    color: white;
    font-size: 22px;
}
</style>
</head>
<body>
Lennart Poettering's cool shop!
Lennart Poettering's cool shop!
Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!
</body>
</html>
"""
