from flask import Flask
app = Flask(__name__)

@app.route('/', )
def hello_world():
  return '<h1>Hello World!\n POPIPOPIPOPOPIPO</h1>'

# @app.route('/about/<username>')
# def about_page(username):
#   # return '<h1>Smurf Cat</h1><img src=https://i.kym-cdn.com/photos/images/newsfeed/002/652/460/d70.jpg height=440px width=440px alt=Smurf Cat/>\n<a href=http://127.0.0.1:5000/>Hello World</a>'

#   return f"<h1>This is the about page of {username}</h1>"