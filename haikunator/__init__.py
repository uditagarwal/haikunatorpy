from random import choice


def haikunate(delimiter='-', tokenLength=4, tokenHex=False, tokenChars='0123456789'):
    """
    Generate Heroku-like random names to use in your applications.
    :param delimiter:
    :param tokenLength:
    :param tokenHex:
    :param tokenChars:
    :return: string
    """

    adjs = [
        "Naughty", "Adorable", "Cute", "Clever", "Mischevious", "Happy", "Loved",
        "Playful", "Energetic", "Wild", "Joyful", "Priceless", "Awesome", "Curious",
        "Protective", "Dominant", "Domestic", "Loyal", "Funny", "Hilarious", "Lucky",
        "Zippy", "Fast", "Wonderful", "Great", "Soft", "Precious", "Quick", "Unique",
        "Brave", "Courageous", "Cuddly", "Snuggly", "Fabulous", "Fantastic", "Goofy",
        "Friendly", "Affectionate", "Giddy", "Jolly", "Jumpy", "Kindhearted",
        "Overjoyed", "Tricky", "Wacky", "Warm", "Youthful", "Young", "Upbeat",
        "Attractive", "Supreme", "Distinct", "Huggable", "Super", "Wide-Eyed",
        "Pleasent", "Strong"
    ]

    nouns = [
        "Lucy", "Daisy", "Molly", "Lola", "Sophie", "Sadie", "Maggie", "Chloe",
        "Bailey", "Roxy", "Zoey", "Lily", "Luna", "Coco", "Stella", "Gracie",
        "Abby", "Penny", "Zoe", "Ginger", "Ruby", "Rosie", "Lilly", "Ellie",
        "Mia", "Sasha", "Lulu", "Pepper", "Nala", "Lexi", "Lady", "Emma",
        "Riley", "Dixie", "Annie", "Maddie", "Piper", "Princess", "Izzy",
        "Maya", "Olive", "Cookie", "Roxie", "Angel", "Belle", "Layla", "Missy",
        "Cali", "Honey", "Millie", "Harley", "Marley", "Holly", "Kona",
        "Shelby", "Jasmine", "Ella", "Charlie", "Minnie", "Willow", "Phoebe",
        "Callie", "Scout", "Katie", "Dakota", "Sugar", "Sandy", "Josie", "Macy",
        "Trixie", "Winnie", "Peanut", "Mimi", "Hazel", "Mocha", "Cleo", "Hannah",
        "Athena", "Lacey", "Sassy", "Lucky", "Bonnie", "Allie", "Brandy",
        "Sydney", "Casey", "Gigi", "Baby", "Madison", "Heidi", "Sally",
        "Shadow", "Cocoa", "Pebbles", "Misty", "Nikki", "Lexie", "Grace",
        "Sierra", "Max", "Buddy", "Charlie", "Jack", "Cooper", "Rocky", "Toby",
        "Tucker", "Jake", "Bear", "Duke", "Teddy", "Oliver", "Riley", "Bailey",
        "Bentley", "Milo", "Buster", "Cody", "Dexter", "Winston", "Murphy",
        "Leo", "Lucky", "Oscar", "Louie", "Zeus", "Henry", "Sam", "Harley",
        "Baxter", "Gus", "Sammy", "Jackson", "Bruno", "Diesel", "Jax", "Gizmo",
        "Bandit", "Rusty", "Marley", "Jasper", "Brody", "Roscoe", "Hank", "Otis",
        "Bo", "Joey", "Beau", "Ollie", "Tank", "Shadow", "Peanut", "Hunter",
        "Scout", "Blue", "Rocco", "Simba", "Tyson", "Ziggy", "Boomer",
        "Romeo", "Apollo", "Ace", "Luke", "Rex", "Finn", "Chance", "Rudy",
        "Loki", "Moose", "George", "Samson", "Coco", "Benny", "Thor", "Rufus",
        "Prince", "Chester", "Brutus", "Scooter", "Chico", "Spike", "Gunner",
        "Sparky", "Mickey", "Kobe", "Chase", "Oreo", "Frankie", "Mac", "Benji",
        "Bubba", "Champ", "Brady", "Elvis", "Copper", "Cash", "Archie", "Walter"
    ]

    if tokenHex:
        tokenChars = '0123456789abcdef'

    adj = choice(adjs)
    noun = choice(nouns)
    token = ''.join(choice(tokenChars) for _ in range(tokenLength))

    sections = [adj, noun, token]
    return delimiter.join(filter(None, sections))
