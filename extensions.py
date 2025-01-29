# extensions.py
from flask_socketio import SocketIO

# Create a global instance of SocketIO (but don't bind it to an app yet)
socketio = SocketIO(cors_allowed_origins="*")
