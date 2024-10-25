from flask import Flask, render_template
from flask_session import Session
from perfils.expert import expert_bp
from perfils.curios import curios_bp
from perfils.pragmatic import pragmatic_bp
from perfils.ocasional import ocasional_bp

def crear_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SESSION_TYPE'] = 'filesystem'  # Store session data on the server (you can also use Redis, Memcached, etc.)
    Session(app)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    app.register_blueprint(expert_bp)
    app.register_blueprint(curios_bp)
    app.register_blueprint(pragmatic_bp)
    app.register_blueprint(ocasional_bp)

    return app

if __name__ == "__main__":
    app = crear_app()
    app.run(debug=True)