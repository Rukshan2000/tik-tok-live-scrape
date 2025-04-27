from app import create_app
from tiktok.client import run_tiktok_client
from threading import Thread

if __name__ == '__main__':
    # Start TikTok client in a thread (will wait for username)
    tiktok_thread = Thread(target=run_tiktok_client)
    tiktok_thread.daemon = True
    tiktok_thread.start()
    
    app = create_app()
    app.run(host='0.0.0.0', port=5000)