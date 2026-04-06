"""
Simple Python Web Application
Uses Flask to create a REST API
"""

from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
app.config['VERSION'] = '1.0.0'

# Routes
@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Python Application',
        'status': 'success',
        'timestamp': datetime.now().isoformat(),
        'version': app.config['VERSION']
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/greet', methods=['POST'])
def greet():
    """Greeting endpoint"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({
            'error': 'Missing name field',
            'status': 'error'
        }), 400
    
    name = data['name']
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/info', methods=['GET'])
def info():
    """Application info endpoint"""
    return jsonify({
        'name': 'Python Application',
        'version': app.config['VERSION'],
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'timestamp': datetime.now().isoformat()
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 'error'
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status': 'error'
    }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
