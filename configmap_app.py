from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    production_env = os.environ.get('PROD_ENV', 'unknown')
    dns_ip = os.environ.get('DNS_IP', 'Unknown')
    
    greeting = ""
    if dns_ip == "8.8.8.8":
        greeting = "Namaste India!!!"
    elif dns_ip == "114.114.115.115":
        greeting = "欢迎来到中国!!!"
    elif dns_ip == "24.19.134.239":
        greeting = "Welcome to the USA!!!"
    elif dns_ip == "202.248.37.74":
        greeting = "日本へようこそ!!!"
    else:
        greeting = "Hello!"
    
    return f"{greeting} .This is {production_env} environment. DNS IP used will be : {dns_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

