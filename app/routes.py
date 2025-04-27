from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from tiktok.data import comments, recent_gifts, gifter_coins, gifter_avatars, data_lock, reset_data
from tiktok.utils import get_animation_class, get_remaining_time, DEFAULT_AVATAR, tiktok_username, reset_match, match_end_time
from tiktok.client import initialize_client
from threading import Thread

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def display_dashboard():
    global tiktok_username
    if request.method == 'POST':
        # Handle username form submission
        new_username = request.form.get('username')
        if new_username and new_username.startswith('@'):
            tiktok_username = new_username
            # Reinitialize TikTok client in a separate thread
            Thread(target=initialize_client, args=(tiktok_username,)).start()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({"message": f"Connected to: {new_username}"})
            return redirect(url_for('main.display_dashboard'))
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({"message": "Invalid username. Please use format @username"}), 400
            return redirect(url_for('main.display_dashboard'))
    
    with data_lock:
        sorted_gifters = sorted(gifter_coins.items(), key=lambda x: x[1], reverse=True)
        top_gifters = [{
            "name": name,
            "coins": coins,
            "avatar": gifter_avatars.get(name, DEFAULT_AVATAR),
            "animation_class": get_animation_class(coins)
        } for name, coins in sorted_gifters[:5]]
        
        mvp = None
        if sorted_gifters:
            top_gifter = sorted_gifters[0]
            mvp = {
                "name": top_gifter[0],
                "coins": top_gifter[1],
                "avatar": gifter_avatars.get(top_gifter[0], DEFAULT_AVATAR),
                "animation_class": get_animation_class(top_gifter[1])
            }
        
        return render_template(
            'dashboard.html',
            username=tiktok_username if tiktok_username else "Not set",
            match_time=get_remaining_time(match_end_time),
            mvp=mvp,
            top_gifters=top_gifters,
            recent_gifts=recent_gifts,
            comments=comments[-20:][::-1]
        )

@main.route('/mvp')
def display_mvp_only():
    with data_lock:
        sorted_gifters = sorted(gifter_coins.items(), key=lambda x: x[1], reverse=True)
        mvp = None
        if sorted_gifters:
            top_gifter = sorted_gifters[0]
            mvp = {
                "name": top_gifter[0],
                "coins": top_gifter[1],
                "avatar": gifter_avatars.get(top_gifter[0], DEFAULT_AVATAR),
                "animation_class": get_animation_class(top_gifter[1])
            }
        
        return render_template('mvp.html', mvp=mvp)

@main.route('/reset', methods=['POST'])
def reset_dashboard():
    """Reset all data and match timer."""
    reset_data()
    reset_match()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({"message": "Dashboard reset successfully"})
    return redirect(url_for('main.display_dashboard'))