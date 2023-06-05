from flask import Flask , url_for

app = Flask(__name__)

@app.route('/')
def intro():
    return "Hello World"

@app.route('/user/<username>')
def user_info(username):
    return f'Welcome. {username}!'

if __name__ == '__main__':
    with app.test_request_context():
        index_url = url_for('intro')
        profile_url = url_for('user_info', username = "satya")

        print(index_url)
        print(profile_url)