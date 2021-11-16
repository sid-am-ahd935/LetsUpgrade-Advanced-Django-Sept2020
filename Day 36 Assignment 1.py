from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

import os;
#Use Before Starting The POST request
#export OAUTHLIB_INSECURE_TRANSPORT=1
#When doing from The Terminal Itself.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"]= '1'

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "why is secret key even a thing"
else:
    from model import app
    
github_blueprint = make_github_blueprint(client_id= 'f2be1e0c7a4808da542a', client_secret= '574646a1a338edb59b4cf9175db6d95df66f3d86')

app.register_blueprint(github_blueprint,url_prefix='/github/login')

@app.route('/github')
def github_login():
    
    if  not github.authorized:
        return redirect(url_for('github.login'))
    account_info = github.get('/user')
    
    if account_info.ok:
        account_info_json = account_info.json()
        return f"<h1>Your GitHub Name: {account_info_json['login']} Is Logged In.</h1>"
        
    return "<h1> Request </h1>"

if __name__ == "__main__":
    app.run(port=9080, debug=True)
