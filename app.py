from flask import Flask

# יצירת אפליקציה
app = Flask(__name__)

# יצירת route לדף הבית
@app.route('/')
def home():
    return ף"Flasks!"

# הפעלת האפליקציה
if __name__ == '__main__':
    app.run(debug=True)

