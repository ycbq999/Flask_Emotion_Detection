from flask import Flask
from myapp import views

app = Flask(__name__) # webserver gateway interface (WSGI)


# @app.route('/') # decorator
# def index():
#     return "<h1>Welcome to Face Expression detection web App</h1>"



app.add_url_rule(rule = '/', endpoint = 'home', view_func = views.index)
app.add_url_rule(rule = '/application', endpoint = 'web_app', view_func = views.web_app)
app.add_url_rule(rule = '/application/emo_detection/', 
                 endpoint = 'emo_detection', 
                 view_func = views.emo_detection,
                 methods=['GET','POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)