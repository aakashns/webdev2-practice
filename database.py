from sqlalchemy import create_engine
import os

engine = create_engine(
    os.environ['DB_CONNECTION_STRING'],
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

if __name__ == '__main__':
  with engine.connect() as conn:
    result = conn.execute('select * from jobs')
    print(list(result.mappings()))