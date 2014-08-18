from application import app

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///snsdb?instance=rukeon07:rukeon07',
    migration_directory = 'migrations'
))
