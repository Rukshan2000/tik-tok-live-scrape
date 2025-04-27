from app import create_app
from tiktok.client import run_tiktok_client
from threading import Thread

# Start TikTok client (even when using gunicorn)
tiktok_thread = Thread(target=run_tiktok_client)
tiktok_thread.daemon = True
tiktok_thread.start()

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
