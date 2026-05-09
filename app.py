from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    
    if request.method == "POST":
        name = request.form.get("name", "")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Flask Page</title>
        <style>
            body {{
                font-family: Arial;
                text-align: center;
                margin-top: 50px;
            }}
            input, button {{
                padding: 10px;
                margin: 5px;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to Your Flask Page</h1>
        
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <button type="submit">Submit</button>
        </form>

        {"<h2>HELLO There, " + name + "!</h2>" if name else ""}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
