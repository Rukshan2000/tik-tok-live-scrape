from datetime import datetime
from tiktok.utils import get_animation_class, get_avatar_base64, GIFT_COIN_VALUES, DEFAULT_COIN_VALUE
from tiktok.data import comments, recent_gifts, gifter_coins, gifter_avatars, data_lock

async def handle_comment(event, client):
    try:
        user = getattr(event, 'user', None)
        if not user:
            print("No user in comment event")
            return
        
        nickname = getattr(user, 'nick_name', None) or getattr(user, 'nickname', 'Unknown')
        
        avatar_base64 = await get_avatar_base64(user, client)
        
        with data_lock:
            comment_data = {
                "user": nickname,
                "text": event.comment,
                "time": datetime.now().strftime("%H:%M:%S"),
                "avatar": avatar_base64
            }
            comments.append(comment_data)
            if len(comments) > 100:
                comments.pop(0)
        print(f"{nickname} -> {event.comment}")
    except Exception as e:
        print(f"Error processing comment: {e}")
    try:
        avatar_base64 = await get_avatar_base64(event.user, client)
        with data_lock:
            comment_data = {
                "user": event.user.nickname,
                "text": event.comment,
                "time": datetime.now().strftime("%H:%M:%S"),
                "avatar": avatar_base64
            }
            comments.append(comment_data)
            if len(comments) > 100:
                comments.pop(0)
        print(f"{event.user.nickname} -> {event.comment}")
    except Exception as e:
        print(f"Error processing comment: {e}")

async def handle_gift(event, client):
    try:
        coin_value = GIFT_COIN_VALUES.get(event.gift.name, DEFAULT_COIN_VALUE)
        total_coins = coin_value
        if hasattr(event.gift, 'diamond_count') and event.gift.diamond_count > 0:
            total_coins = event.gift.diamond_count
        if event.gift.streakable and not event.streaking:
            total_coins *= event.repeat_count
        
        avatar_base64 = await get_avatar_base64(event.user, client)
        
        with data_lock:
            gifter_coins[event.user.nickname] += total_coins
            if event.user.nickname not in gifter_avatars:
                gifter_avatars[event.user.nickname] = avatar_base64
            
            gift_data = {
                "user": event.user.nickname,
                "name": event.gift.name,
                "count": event.repeat_count,
                "coins": total_coins,
                "time": datetime.now().strftime("%H:%M:%S"),
                "avatar": avatar_base64,
                "animation_class": get_animation_class(total_coins)
            }
            recent_gifts.append(gift_data)
            if len(recent_gifts) > 20:
                recent_gifts.pop(0)
        
        print(f"{event.user.nickname} sent {event.gift.name} worth {total_coins} coins (Total: {gifter_coins[event.user.nickname]})")
    except Exception as e:
        print(f"Error processing gift: {e}")

def handle_join(event):
    try:
        user = getattr(event, 'user', None)
        if not user:
            print("No user in join event")
            return
        
        nickname = getattr(user, 'nick_name', None) or getattr(user, 'nickname', 'Unknown')
        print(f"{nickname} joined the stream!")
    except Exception as e:
        print(f"Error processing join: {e}")
