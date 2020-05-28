from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'edward cho',
        'title':'Blog Post 1',
        'content':'first post content',
        'date_posted':'April 20, 2020'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'second post content',
        'date_posted':'April 22, 2020'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')


if __name__ == "__main__":
    app.run(debug=True)
