from flask import Flask, send_from_directory, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """Serve the main quiz page"""
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/images/<path:filename>')
def serve_images(filename):
    """Serve images from the images directory"""
    images_dir = os.path.join(BASE_DIR, 'images')
    return send_from_directory(images_dir, filename)

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve any other static files"""
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    print("🚀 Starting Kids Electronics Quiz Server...")
    print("📚 Quiz Features:")
    print("   ✅ 15 Interactive Questions")
    print("   ✅ Multiple Choice & Matching Questions")
    print("   ✅ Kid-Friendly Design")
    print("   ✅ Multiple Students Support")
    print("   ✅ Instant Feedback")
    print("\n🌐 Server will be accessible to all students once deployed!")
    
    # Run the server on all interfaces so it can be accessed externally
    app.run(host='0.0.0.0', port=8080, debug=True)

