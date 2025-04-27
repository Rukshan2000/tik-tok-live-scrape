from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, GiftEvent, JoinEvent
import asyncio
from tiktok.events import handle_comment, handle_gift, handle_join
from tiktok.utils import tiktok_username

# Global client (initially None)
client = None

def initialize_client(username):
    """Initialize or reinitialize the TikTok client with a new username."""
    global client
    if client is not None:
        # Stop existing client if running
        try:
            client.disconnect()
            print(f"Disconnected previous client for {client.unique_id}")
        except Exception as e:
            print(f"Error disconnecting previous client: {e}")
    
    client = TikTokLiveClient(unique_id=username)
    
    # Register event handlers
    @client.on(ConnectEvent)
    async def on_connect(event):
        print(f"Connected to @{client.unique_id} (Room ID: {client.room_id})")

    @client.on(CommentEvent)
    async def on_comment(event):
        await handle_comment(event, client)

    @client.on(GiftEvent)
    async def on_gift(event):
        await handle_gift(event, client)

    @client.on(JoinEvent)
    async def on_join(event):
        handle_join(event)
    
    # Start the client
    try:
        asyncio.run(client.run())  # This will run the client in the current event loop
    except Exception as e:
        print(f"Error running client for {username}: {e}")


def run_tiktok_client():
    """Run the TikTok client if a username is set."""
    global tiktok_username
    if tiktok_username is None:
        print("No username set. Please set a username via the dashboard.")
        return
    
    initialize_client(tiktok_username)