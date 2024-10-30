import discord
from discord import app_commands
import requests
import random
import asyncio

# Replace with your bot's token and Imgur client ID
DISCORD_TOKEN = 'redacted'
IMGUR_CLIENT_ID = 'redacted'
TARGET_BOT_NAME = 'FOOT DEX'
TARGET_BOT_DISCRIMINATOR = '1511'
TARGET_USER_NAME = 'codingismypassion'
FILE_PATH = __file__

# Define intents to allow the bot to read messages and member information
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # To find the target user by name

# Define the bot class using discord.Client instead of commands.Bot
class MyBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot(intents=intents)

# Jokes list for the joke command
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you get when you cross a snowman with a vampire? Frostbite.",
    "Why was the math book sad? It had too many problems.",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "How does a penguin build its house? Igloos it together.",
    "Why did the bicycle fall over? It was two-tired.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "Why don't eggs tell jokes? They might crack up.",
    "What do you call a factory that makes good products? A satisfactory.",
    "Why did the coffee file a police report? It got mugged.",
    "What's orange and sounds like a parrot? A carrot.",
    "How do you organize a space party? You planet.",
    "What do you call a boomerang that won't come back? A stick.",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
    "Why was the big cat disqualified from the race? Because it was a cheetah.",
    "Why don't oysters donate to charity? Because they are shellfish.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why do cows wear bells? Because their horns don't work.",
    "Why don't sharks like fast food? Because they can't catch it.",
    "Why don't koalas count as bears? They don't have the right koalafications.",
    "What do you call a magic dog? A labracadabrador.",
    "What did the janitor say when he jumped out of the closet? Supplies!",
    "Why don't some fish play piano? Because you can't tuna fish.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "How does a tree get online? It logs in.",
    "Why are elevator jokes so classic? Because they work on many levels.",
    "What does a nosy pepper do? It gets jalapeño business.",
    "Why was the broom late? It swept in.",
    "What did the buffalo say to his son when he left? Bison.",
    "Why do bananas never get lonely? Because they hang out in bunches.",
    "What did the grape do when it got stepped on? Nothing, but it let out a little wine.",
    "Why did the cookie go to the doctor? Because it felt crummy.",
    "Why was the music teacher so good at baseball? She had perfect pitch.",
    "What did the pirate say on his 80th birthday? Aye matey!",
    "Why don't melons get married? Because they cantaloupe.",
    "Why did the picture go to jail? Because it was framed.",
    "What do you call a fish without eyes? Fsh.",
    "Why did the teddy bear say no to dessert? Because he was stuffed.",
    "What did one wall say to the other wall? I'll meet you at the corner.",
    "Why was the belt arrested? It was holding up a pair of pants.",
    "Why don't vampires go to barbecues? They don't like steak.",
    "What did the grape say when it got crushed? Nothing, it just let out a little wine.",
    "What kind of tree fits in your hand? A palm tree.",
    "How do you make a tissue dance? You put a little boogie in it.",
    "Why was the equal sign so humble? Because he wasn't less than or greater than anyone else.",
    "Why don't you ever see elephants hiding in trees? Because they're so good at it.",
    "Why did the frog take the bus to work? His car got toad.",
    "Why did the man put his money in the blender? He wanted to make some liquid assets.",
    "Why did the gym close down? It just didn't work out.",
    "What do you call an alligator in a vest? An investigator.",
    "What do you get when you cross a snowman and a dog? Frostbite.",
    "Why did the golfer bring extra socks? In case he got a hole in one.",
    "Why was Cinderella so bad at soccer? She kept running away from the ball.",
    "Why did the man put his money in the blender? He wanted to make liquid assets.",
    "Why don't some fish play basketball? Because they're afraid of the net.",
    "Why did the chicken go to the seance? To talk to the other side.",
    "What do you call a pile of cats? A meowtain.",
    "What did the fish say when it swam into a wall? Dam.",
    "Why was the broom late? It swept in.",
    "What do you call fake spaghetti? An impasta.",
    "Why don't programmers like nature? It has too many bugs.",
    "What did the Atlantic Ocean say to the Pacific Ocean? Nothing, they just waved.",
    "Why did the bank teller go broke? He lost interest.",
    "Why don't we see elephants hiding in trees? Because they're really good at it.",
    "Why can't you hear a pterodactyl go to the bathroom? Because the 'P' is silent.",
    "Why did the cookie go to the doctor? It felt crummy.",
    "Why was the belt arrested? It was holding up a pair of pants.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "What do you call an illegally parked frog? Toad.",
    "Why was the computer cold? It left its Windows open.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why was the math book sad? It had too many problems.",
    "What kind of shoes do ninjas wear? Sneakers.",
    "Why can't you give Elsa a balloon? Because she will let it go.",
    "Why don't crabs give to charity? Because they're shellfish.",
    "How do you catch a squirrel? Climb a tree and act like a nut.",
    "Why did the coffee file a police report? It got mugged.",
    "Why did the orange stop? It ran out of juice.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "Why do ghosts love elevators? Because they lift their spirits.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    "How do you make holy water? You boil the hell out of it.",
    "What kind of tea is hard to swallow? Reality.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "What do you call a snobbish criminal going downstairs? A condescending con descending.",
    "Why do chicken coops only have two doors? Because if they had four, they'd be chicken sedans!",
    "What did the janitor say when he jumped out of the closet? Supplies!",
    "What did one plate say to the other? Lunch is on me.",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "What did the tree say to autumn? Leaf me alone!",
    "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field.",
    "What do you call a broken pencil? Pointless.",
    "Why do golfers always bring an extra pair of pants? In case they get a hole in one!",
    "Why don't some fish play basketball? Because they're afraid of the net!",
    "What happens to a frog's car when it breaks down? It gets toad away!",
    "Why don't some fish like playing cards? They don't want to get caught!",
    "What do you call a fish who practices medicine? A sturgeon!",
    "Why did the banker break up with their partner? They lost interest.",
    "Why did the hipster burn their mouth on coffee? They drank it before it was cool.",
    "Why are ghosts bad at lying? Because they are too transparent.",
    "How does a vampire start a letter? Tomb it may concern...",
    "Why did the stadium get so hot? Because all the fans left!",
    "What did the janitor say to the elevator? I'll lift you up!",
    "What do you call a can opener that doesn't work? A can't opener.",
    "Why was the student's report card wet? It was below sea level.",
    "Why do bees have sticky hair? Because they use honeycombs!",
    "What did the 0 say to the 8? Nice belt!",
    "Why do elephants never use computers? They're afraid of the mouse!",
    "How do you make a lemon drop? Just let it fall!",
    "Why did the teacher go to the beach? To test the waters!",
    "Why did the bicycle fall over? Because it was two-tired!",
]

# Function to upload image to Imgur
def upload_image_to_imgur(image_url):
    headers = {
        'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'
    }
    data = {
        'image': image_url,
        'type': 'url'
    }
    response = requests.post('https://api.imgur.com/3/image', headers=headers, data=data)
    
    if response.status_code == 200:
        imgur_link = response.json()['data']['link']
        return imgur_link
    else:
        return None

# Function to create Google Lens reverse image search URL
def google_lens_reverse_image_search_url(image_url):
    lens_url = f"https://lens.google.com/uploadbyurl?url={image_url}"
    return lens_url

# Function to save jokes to the file
def save_jokes():
    with open(FILE_PATH, 'r') as file:
        lines = file.readlines()

    new_lines = []
    inside_joke_block = False

    for line in lines:
        if line.strip().startswith('jokes = ['):
            new_lines.append('jokes = [\n')
            inside_joke_block = True
            for joke in jokes:
                new_lines.append(f'    "{joke}",\n')
        elif inside_joke_block and line.strip().startswith(']'):
            inside_joke_block = False
            new_lines.append(']\n')
        elif not inside_joke_block:
            new_lines.append(line)

    with open(FILE_PATH, 'w') as file:
        file.writelines(new_lines)

# Slash command to tell a joke
@bot.tree.command(name='joke', description='Tell a random joke')
async def joke(interaction: discord.Interaction):
    if jokes:
        joke_message = random.choice(jokes)
        await interaction.response.send_message(joke_message)
    else:
        await interaction.response.send_message("No jokes available. Please submit some!")

# Slash command to submit a joke
@bot.tree.command(name='submit_joke', description='Submit your own joke')
async def submit_joke(interaction: discord.Interaction, joke_text: str):
    new_joke = f"{joke_text} ~ {interaction.user.display_name}"

    if new_joke in jokes:
        await interaction.response.send_message("This joke already exists. Please submit a different one.")
        return

    jokes.append(new_joke)
    save_jokes()
    await interaction.response.send_message(f"Thank you for your joke, {interaction.user.display_name}!")

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Triggered when a message is sent in the channel
@bot.event
async def on_message(message):
    await bot.process_commands(message)  # Ensure bot commands still work

    # Check if the message was sent by the bot "FOOT DEX#1511"
    if message.author.bot and message.author.name == TARGET_BOT_NAME and message.author.discriminator == TARGET_BOT_DISCRIMINATOR:
        if message.attachments:
            image = message.attachments[0]

            if image.filename.endswith(('png', 'jpg', 'jpeg')):
                image_url = image.url

                imgur_url = upload_image_to_imgur(image_url)

                if imgur_url:
                    lens_url = google_lens_reverse_image_search_url(imgur_url)

                    target_user = discord.utils.get(message.guild.members, name=TARGET_USER_NAME)
                    if target_user:
                        await target_user.send(f"Here is the Google Lens Reverse Image Search link for the image from FOOT DEX#1511:\n{lens_url}")
                    else:
                        print(f"User {TARGET_USER_NAME} not found in the server.")
                else:
                    print("Failed to upload image to Imgur.")
        else:
            print("No image found in FOOT DEX's message.")

# Main function to run the bot
def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(bot.start(DISCORD_TOKEN))
    except discord.LoginFailure as e:
        print(f"Failed to log in: {e}")
    except KeyboardInterrupt:
        print("Received exit signal, shutting down...")
    finally:
        loop.run_until_complete(bot.close())
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()

if __name__ == "__main__":
    main()