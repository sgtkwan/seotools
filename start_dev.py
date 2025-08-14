#!/usr/bin/env python3
"""
Development startup script for Flask Keyword Classifier
This script sets up the development environment and runs the app
"""

import os
import sys

# Set development environment
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_APP'] = 'app.py'

# Check if .env file exists
if not os.path.exists('.env'):
    print("Warning: No .env file found. Please create one based on env.example")
    print("Required environment variables:")
    print("- GOOGLE_API_KEY: Your Google Gemini API key")
    print("- SECRET_KEY: A secret key for Flask sessions")
    print()

# Import and run the app
try:
    from app import app
    print("Starting Flask development server...")
    print("App will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
    
except ImportError as e:
    print(f"Error importing app: {e}")
    print("Make sure you have installed all dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Error starting app: {e}")
    sys.exit(1)
