from app import app, db
from app.models import Laundry, Time, Search

@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'Outgoing': Outgoing}