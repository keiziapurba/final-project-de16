from sqlalchemy import create_engine

class Connector():
    def __init__(self):
        pass

    def connect_mysql(self, user, password, host, db, port):
        engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
            'root', 'prbKei29_', 'localhost', '3306', 'staging_fpde16'
        ))
        return engine
    
    def connect_postgres(self, user, password, host, db, port):
        engine = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            user, 'prbKei29_', 'localhost', '5432', 'postgres'
        ))
        return engine 