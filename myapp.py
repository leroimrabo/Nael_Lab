from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    # Pass dynamic content into your template
    title = "Welcome to my Python Webpage!"
    items = ["Python", "Flask", "Jinja Templates"]
    return render_template('index.html', page_title=title, tech_stack=items)

if __name__ == '__main__':
    # Run the web server locally
    app.run(debug=True, port=8000)
