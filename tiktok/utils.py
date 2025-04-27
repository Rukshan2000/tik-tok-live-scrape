
from datetime import datetime, timedelta
import base64

# Dynamic username (initially None, set via dashboard)
tiktok_username = None

# Match configuration
MATCH_DURATION = timedelta(minutes=10)
match_start_time = datetime.now()
match_end_time = match_start_time + MATCH_DURATION

DEFAULT_AVATAR = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI0ZFMkM1NSIgZD0iTTEyIDJDNi40NzcgMiAyIDYuNDc3IDIgMTJzNC40NzcgMTAgMTAgMTAgMTAtNC40NzcgMTAtMTBTMTcuNTIzIDIgMTIgMnptMCAxOC44NTdjLTQuODgxIDAtOC43NTctMy45MTYtOC43NTctOC43NTdTNy4xNTkgMy4zNDMgMTIgMy4zNDNzOC43NTcgMy45MTYgOC43NTcgOC43NTctMy45MTYgOC43NTctOC43NTcgOC43NTd6TTEyIDYuNTQzYy0xLjYwNSAwLTIuOTE0IDEuMzA5LTIuOTE0IDIuOTE0UzEwLjM5NSAxMi4zNyAxMiAxMi4zN3MyLjkxNC0xLjMwOSAyLjkxNC0yLjkxNFMxMy42MDUgNi41NDMgMTIgNi41NDN6bTAgNC43NzFjLS45ODcgMC0xLjc4Ni0uOC0xLjc4Ni0xLjc4NlMxMS4wMTMgNy43NDMgMTIgNy43NDNzMS43ODYuOCAxLjc4NiAxLjc4Ni0uOCAxLjc4NS0xLjc4NiAxLjc4NXpNNy4wMzQgMTYuNDdjLjY3Ni0xLjU0IDIuMDk3LTIuNTcgMy43MDYtMi41N2gxLjUyYzEuNjA5IDAgMy4wMyAxLjAzIDMuNzA2IDIuNTctLjQ5Mi4yMjctMS4wNTguMzUzLTEuNjQ2LjM1M0g4LjY4Yy0uNTg4IDAtMS4xNTQtLjEyNi0xLjY0Ni0uMzUzeiIvPjwvc3ZnPg=="

GIFT_COIN_VALUES = {"Alien Peace Sign": 1, "Chocolate": 1, "Coffee": 1, "Daisies": 1, "Fire": 1, "Football": 1, "Garden Gnome": 1, "GG": 1, "Heart Me": 1, "Ice Cream Cone": 1, "Lightning Bolt": 1, "Love letter": 1, "Mini Speaker": 1, "Rose": 1, "Squirrel": 1, "Tennis": 1, "TikTok": 1, "Weights": 1, "Baklava": 2, "Chic": 5, "Cornflower": 5, "Cotton's Shell": 5, "Duckling": 5, "Finger Heart": 5, "Hi": 5, "Mic": 5, "Panda": 5, "Pink Shoes": 5, "Thumbs Up": 5, "Waving Hand": 7, "Crocodile": 10, "Dog Bone": 10, "Gamepad": 10, "Lollipop": 10, "Marvin the Monkey": 10, "Maxwell": 10, "Stars Snap": 10, "This is Fire": 10, "Tiny Dinosaur": 10, "Accept this Rose": 15, "Raccoon": 15, "Baby fox": 20, "Perfume": 20, "Applause": 25, "Cry Laugh": 25, "Love": 25, "Made My Day": 25, "OMG": 25, "Plus One": 25, "Hilarious": 29, "Party": 29, "Capybara": 30, "Donuts": 30, "Mirror": 30, "I Love You": 49, "Tea": 50, "Ruby Red": 88, "Cap": 99, "Little Crown": 99, "Hat and Mustache": 99, "My Favorite": 99, "Origami": 99, "Paper Crane": 99, "Bear Love": 100, "Confetti": 100, "Hand Heart": 100, "Umbrella": 150, "Butterfly": 169, "Musical Notes": 169, "Witch's Hat": 177, "Crown": 199, "Flower Festival": 199, "Garland Headpiece": 199, "Goggles": 199, "Hearts": 199, "Indoor Fan": 199, "Love You": 199, "Lock and Key": 199, "Panther Paws": 199, "The Passion Rose": 199, "Pug": 199, "Puppy Love": 199, "Sending Positivity": 199, "Ski Goggles": 199, "Sunglasses": 199, "Travel Trolley": 199, "Tulip Box": 200, "Astronaut": 299, "Boxing Gloves": 299, "Bridal Veil": 299, "Corgi": 299, "Dancing Cactus": 299, "Dash": 299, "Duck": 299, "Elephant Trunk": 299, "Rock 'n' Roll": 299, "Superpower": 299, "Air Dancer": 300, "Birthday Cake": 300, "Tumpeng Rice": 300, "Campfire": 388, "Singing Frogs": 398, "Cotton the Seal": 399, "Flower Flight": 399, "Gamer Cyber Mask": 399, "Good Night": 399, "Sweet Dreams": 399, "Swing": 399, "Marine Trap": 400, "Necklace": 400, "Across the Board": 450, "Coral": 499, "Magic Potion": 499, "Ballet Dancer": 500, "Bronze Gummy": 500, "Gardening": 500, "Make it rain": 500, "Spaghetti Kiss": 500, "Window Basket": 500, "Ice Machine": 538, "Cooper Skates Home": 599, "Happy Weekend": 599, "Record Player": 600, "Dance Together": 699, "Goose": 699, "LOVE Balloon": 699, "Swan": 699, "TikTok Trophy": 699, "Shoes": 700, "Silver Gummy": 750, "Pearl": 800, "Train": 899, "Badminton": 999, "Travel With You": 999, "Dinosaur": 1000, "Disco Ball": 1000, "Email Message": 1000, "Galaxy": 1000, "Gerry the Giraffe": 1000, "Gold Gummy": 1000, "Gold Mine": 1000, "Magic Lamp": 1000, "Mirror Flower": 1000, "Space": 1000, "Watermelon Love": 1000, "Diamond Tree": 1088, "Fireworks": 1088, "Diamond": 1099, "Counting Sheep": 1200, "Gaming Chair": 1200, "Take a Drive": 1200, "Bumper Cars": 1288, "Streamers Set-up": 1400, "Champion": 1500, "Chasing the Dream": 1500, "Diamond Ring": 1500, "Flower Arrangement": 1500, "Garland": 1500, "Drinking Time": 1777, "Tree House": 1799, "Airship": 1999, "Autumn Candle": 1999, "Cooper Flies Home": 1999, "Magic Album": 1999, "Makeup Box": 1999, "Mystery Firework": 1999, "Rabbit": 1999, "Star Adventures": 1999, "Carousel": 2020, "South Korea": 2020, "Whale Diving": 2150, "Jet Ski": 2199, "Music Box": 2399, "Concert": 2888, "Travel": 2888, "Double trouble": 2988, "Mermaid": 2988, "Motorcycle": 2988, "Old Famous Car": 2999, "Superstars": 2999, "Car Drifting": 3000, "Dancing Bears": 3000, "Ferris Wheel": 3000, "Meteor Shower": 3000, "Ringworm": 3000, "Summer Vibes": 3188, "Cooper Swims Home": 3999, "Sakura Train": 3999, "Flower Overflow": 4000, "Spilled Flowers": 4000, "TikTok Volcano": 4000, "Knight": 4088, "Tractor": 4099, "Leon the Kitten": 4888, "Pirate Ship": 4888, "Private Jet": 4888, "Pool Party": 4999, "Beach Hut": 5000, "Bird Whisperer": 5000, "Dancing Adam": 5000, "Draco": 5000, "Ellie the Elephant": 5000, "Flying Jets": 5000, "Unicorn Fantasy": 5000, "Wolf": 5000, "Submarine": 5199, "Cooper's Home": 5999, "Valley Festival": 5999, "Airplane": 6000, "Double Decker": 6000, "Starfish Bay": 6000, "Sports Car": 7000, "Yacht": 7499, "Match Trophy": 7999, "Monster Truck": 7999, "Yachts": 9888, "Aquarius": 9999, "Interstellar": 10000, "Octopus": 10000, "Sunset Speedway": 10000, "Falcon": 10999, "Bungee Jump": 12000, "Convertible Car": 12000, "Frog Prince": 12000, "Mountains": 12000, "Spaceship": 13999, "Castle Skyline": 15000, "Leopard": 15000, "Maggie": 15000, "Peacock": 15000, "Pirate's Ship": 15000, "Planet": 15000, "Pyramids": 15000, "Schoolbus": 15000, "Sparrow": 15000, "Venus": 15000, "Hot Air Balloon": 20000, "Grainfield": 24999, "Kite": 24999, "Snakeskin": 24999, "Night Moon": 30000, "Vatican City": 39999, "Amethyst": 49999, "Diamond Necklace": 99999}

DEFAULT_COIN_VALUE = 1

def get_animation_class(coins):
    if coins >= 30:
        return "animation-20000"
    elif coins >= 20:
        return "animation-10000"
    elif coins >= 10:
        return "animation-5000"
    elif coins >= 5:
        return "animation-2000"
    elif coins >= 1:
        return "animation-1000"
    return ""

def get_remaining_time(match_end_time):
    remaining = match_end_time - datetime.now()
    if remaining.total_seconds() <= 0:
        return "MATCH ENDED"
    minutes, seconds = divmod(int(remaining.total_seconds()), 60)
    return f"{minutes:02d}:{seconds:02d}"

async def get_avatar_base64(user, client):
    try:
        if hasattr(user, 'avatar_thumb'):
            image_bytes = await client.web.fetch_image_data(image=user.avatar_thumb)
            return f"data:image/webp;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
    except Exception as e:
        print(f"Error fetching avatar: {e}")
    return DEFAULT_AVATAR

def reset_match():
    """Reset match timer."""
    global match_start_time, match_end_time
    match_start_time = datetime.now()
    match_end_time = match_start_time + MATCH_DURATION