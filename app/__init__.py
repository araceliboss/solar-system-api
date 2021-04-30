from flask import Flask

#db = #CHANGE ME
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config[""] = False
    app.config[""] = "postgresql+psycopg2://postgres:postgres@localhost:5432/CHANGE_HERE"

    db.init_app(app)
    migrate.init__app(app, db)
    # from we dont know yet 
    # 

    return app
