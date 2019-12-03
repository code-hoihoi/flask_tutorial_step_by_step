"""In this example, we're returning valid HTML code.

If you open this example in your browser, you'll see the page rendered
nicely as a real HTML page. That means that Flask took care of returning
to the client the `Content-Type: 'text/html'`.

**TODO**
Use the list of authors present in the `hello_world` view to
return a <ul> HTML tag containing the authors in the list.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = """
        <html>
            <h1>Welcome to our Library!</h1>
            <ul>
                <li>Edgar A. Poe</li>
                <li>Jorge L. Borges</li>
                <li>Mark Twain</li>
        </html>
    """
    
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    # build an <ul> with authors
    authors_list = "<ul>"
    authors_list += "\n".join([
        "<li>{author}</li>".format(author=author) for author in authors
    ])
    authors_list += "</ul>"
    print(authors_list)
    #return html
    return authors_list
