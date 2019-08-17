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
p {
    margin-top: 2em;
    transform: rotate(3deg);
}
</style>
</head>
<body>
<h1>Lennart Poettering's cool shop!</h1>

<h3>aka Nik &amp; Pria's t-shirt business / cloud.</h3>
<p>
Lennart Poettering's cool shop!
Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!
Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!Lennart Poettering's cool shop!
</p>

</body>
</html>
"""
