from User.user import app
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="192.168.1.66", port = 5000)