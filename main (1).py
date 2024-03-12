import time
import random

def random_kaomoji():
    kaomoji_list = [
        "(^_^)/", "（*＾3＾)/~☆", "(｡♥‿♥｡)", "(¬‿¬)", "( ˘ ³˘)♥", "(´∩｡• ᵕ •｡∩`)", "(✿◠‿◠)", "(≧◡≦)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(◕‿◕✿)",
        "(•‿•)", "(˘⌣˘)", "( ˘ ³˘)", "(｡♥‿♥｡)", "(＾◡＾)っ", "(*^▽^*)", "(¬‿¬ )", "(˘ω˘)", "(*≧ω≦)"
    ]
    return random.choice(kaomoji_list)

def generate_generic_compliment():
    compliments = [
        f"You are the light in my life, brightening even the darkest moments {random_kaomoji()}",
        f"Your love is the anchor that keeps me grounded and secure {random_kaomoji()}",
        f"In the vast ocean of life, you are my guiding star {random_kaomoji()}",
        f"Your kindness and warmth make every day a joyful adventure {random_kaomoji()}",
        f"You are the melody to the song of my heart, bringing harmony to my soul {random_kaomoji()}",
        f"Your smile is a constellation of joy in the night sky of my life {random_kaomoji()}",
        f"In the garden of love, you are the most beautiful blooming flower {random_kaomoji()}",
        f"Your laughter is the sweetest melody, echoing in the chambers of my heart {random_kaomoji()}",
        f"With you, every moment is a page in a beautiful love story {random_kaomoji()}",
        f"Your love is the potion that turns the ordinary into extraordinary {random_kaomoji()}"
    ]
    return random.choice(compliments)

def generate_dark_souls_compliment():
    compliments = [
        f"Like a chosen undead, your presence lights my dark path {random_kaomoji()}",
        f"In the realm of Lordran, you are my sun and stars {random_kaomoji()}",
        f"As resilient as the Ashen One, your love persists {random_kaomoji()}",
        f"You are the flame that keeps the age of fire burning in my heart {random_kaomoji()}",
        f"Just as the bearer of the curse, your love endures the test of time {random_kaomoji()}",
        f"Our love is as unbreakable as Havel's mighty armor {random_kaomoji()}",
        f"You are the Estus that heals the wounds of my soul {random_kaomoji()}",
        f"Our love is a co-op adventure, facing challenges together like true Sunbros {random_kaomoji()}",
        f"Like Solaire seeking his 'Sun,' I find completeness in you {random_kaomoji()}",
        f"As the Fire Keeper tends to the bonfire, you nurture the warmth in my heart {random_kaomoji()}"
    ]
    return random.choice(compliments)

def generate_bloodborne_compliment():
    compliments = [
        f"In the nightmare of our world, you are my guiding moonlight {random_kaomoji()}",
        f"Your love echoes in the Hunter's Dream, a sanctuary in my heart {random_kaomoji()}",
        f"As a hunter of beasts, your courage is unmatched in my eyes {random_kaomoji()}",
        f"Our love transcends the dream, like the bond between hunter and doll {random_kaomoji()}",
        f"Together, we face the eldritch truth of our intertwined destinies {random_kaomoji()}",
        f"Our love is as enduring as the Hunter's Mark, etched into the fabric of time {random_kaomoji()}",
        f"You are my insight, revealing the beauty in the chaos of life {random_kaomoji()}",
        f"Just as the moon phases, our love waxes and wanes, but never fades {random_kaomoji()}",
        f"Your presence is the lantern that guides me through the darkest of nights {random_kaomoji()}",
        f"Like a Blood Gem, your love enhances the strength of my existence {random_kaomoji()}"
    ]
    return random.choice(compliments)

def generate_elden_ring_compliment():
    compliments = [
        f"In the lands between, you are my radiant grace {random_kaomoji()}",
        f"Your love echoes through the shattering skies of the Erdtree {random_kaomoji()}",
        f"As Tarnished as we are, our connection remains untarnished {random_kaomoji()}",
        f"You are the Elden Lord to my tarnished soul, a beacon of hope {random_kaomoji()}",
        f"In the grand tapestry of the Lands Between, our love is an eternal flame {random_kaomoji()}",
        f"Just as the Roundtable Holders unite, our love forms an unbreakable alliance {random_kaomoji()}",
        f"Your love is a blessing, like the divine grace of the Erdtree {random_kaomoji()}",
        f"We are like a pair of Runes, eternally etched into the fabric of fate {random_kaomoji()}",
        f"In the cycle of the Erdtree, our love is an unending, beautiful refrain {random_kaomoji()}",
        f"As the Erdtree stands tall, so does our love, reaching new heights {random_kaomoji()}"
    ]
    return random.choice(compliments)

def generate_astronomy_compliment():
    compliments = [
        f"Your love is like the North Star, a constant and guiding light in my life {random_kaomoji()}",
        f"Our connection is as celestial as the dance of the planets in the night sky {random_kaomoji()}",
        f"Just as the moon affects the tides, your presence influences the ebb and flow of my emotions {random_kaomoji()}",
        f"In the vast cosmos of love, you are the brightest constellation in my heart {random_kaomoji()}",
        f"Our love is a cosmic journey, exploring the galaxies of happiness together {random_kaomoji()}",
        f"Like a comet's tail, your love leaves a trail of beauty in the canvas of my life {random_kaomoji()}",
        f"You are my celestial muse, inspiring the most beautiful constellations in my heart {random_kaomoji()}",
        f"As the stars align in the sky, so does my heart align with yours in perfect harmony {random_kaomoji()}",
        f"Your love is the gravitational force that keeps my heart orbiting around yours {random_kaomoji()}",
        f"In the galaxy of emotions, our love shines as a radiant supernova {random_kaomoji()}"
    ]
    return random.choice(compliments)

def praise_lothric():
    while True:
        print("*:･ﾟ✧Choose the type of compliment*:･ﾟ✧:")
        print(f"1 ♥ Generic {random_kaomoji()}")
        print(f"2 ♥ Dark Souls {random_kaomoji()}")
        print(f"3 ♥ Bloodborne {random_kaomoji()}")
        print(f"4 ♥ Elden Ring {random_kaomoji()}")
        print(f"5 ♥ Astronomy {random_kaomoji()}")
        print(f"6 ♥ Quit {random_kaomoji()}")
        
        choice = input("*:･ﾟ✧Enter the number corresponding to your choice (1-6)*:･ﾟ✧: ")

        if choice == "1":
            compliment = generate_generic_compliment()
        elif choice == "2":
            compliment = generate_dark_souls_compliment()
        elif choice == "3":
            compliment = generate_bloodborne_compliment()
        elif choice == "4":
            compliment = generate_elden_ring_compliment()
        elif choice == "5":
            compliment = generate_astronomy_compliment()
        elif choice == "6":
            print("Goodbye! ❤️")
            break
        else:
            print("*:･ﾟ✧Invalid choice*:･ﾟ✧")
            compliment = generate_generic_compliment()

        print(f"\n⭐️✨🌟 Praise for Lothric 🌟✨⭐️")
        time.sleep(1)
        print(f"{compliment} {random_kaomoji()}")
        time.sleep(1)
        print(f"*:･ﾟ✧I love you to the {random_kaomoji()}*:･ﾟ✧")  
        time.sleep(1)
        print(f"*:･ﾟ✧❤️❤️❤️ Forever yours, {random_kaomoji()}")
        
        return_menu = input("*:･ﾟ✧Do you want to return to the menu? (yes/no)*:･ﾟ✧: ")
        if return_menu.lower() != 'yes':
            print("*:･ﾟ✧Goodbye! ❤️*:･ﾟ✧")
            break

# Call the function to praise Lothric
praise_lothric()
