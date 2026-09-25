from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page (handles both viewing the page and submitting the form)
@app.route('/', methods=['GET', 'POST'])  # <-- Removed the url_value_preprocessor decorator
def home():
    greeting = None
    
    if request.method == 'POST':
        # Retrieve the 'username' submitted from the HTML form
        user_name = request.form.get('username')
        
        # Process the data using Python logic
        if user_name:
            greeting = f"Hello, {user_name}! Securely processed by the Python backend."
            
    # Send the backend variables over to the HTML frontend template
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    # Setting host="0.0.0.0" makes the server accessible on your local network
    app.run(host="0.0.0.0", port=5000, debug=True)
