from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    version = os.environ.get('APP_VERSION', '1.0')
    return f'''
    🚀 Hello World from Optimus!
    '''

@app.route('/health')
def health_check():
    return {
        'status': 'healthy', 
        'message': 'Optimus Python app is running',
        'version': os.environ.get('APP_VERSION', '1.0')
    }

@app.route('/info')
def info():
    return {
        'app': 'Optimus Python Hello World',
        'deployed_via': 'GitHub Actions',
        'aws_region': 'us-west-2',
        'account': '137360334857'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)