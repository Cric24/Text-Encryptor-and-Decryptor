from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    decrypted_text = ""

    if request.method == 'POST':
        action = request.form.get('action')
        text = request.form.get('text')
        
        if action == 'Encrypt' and text:
            encrypted_text = cipher_suite.encrypt(text.encode()).decode()
        elif action == 'Decrypt' and text:
            try:
                decrypted_text = cipher_suite.decrypt(text.encode()).decode()
            except Exception as e:
                decrypted_text = f"Error: {str(e)}"

    return render_template('index.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
