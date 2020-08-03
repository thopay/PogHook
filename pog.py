from discord_webhook import DiscordWebhook, DiscordEmbed
import random, time

def kodai(webhook_url, product_image, store, checkout_speed, product, size, profile, group, date):
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title=':rocket:   Kodai Success   :rocket:', color=7011988)
    embed.set_thumbnail(url=product_image)
    embed.add_embed_field(name='Store', value=store, inline=True)
    embed.add_embed_field(name='Checkout Speed', value=checkout_speed, inline=True)
    embed.add_embed_field(name='Product', value=product, inline=False)
    embed.add_embed_field(name='Size', value=size, inline=True)
    embed.add_embed_field(name='Profile', value='||'+profile+'|| :flag_us:', inline=True)
    embed.set_footer(text='KodaiAIO ― '+group+' • ['+date+']', icon_url="https://images-ext-2.discordapp.net/external/krVmbzqvZ1lgEThP_2eA0D60X_9xKP8d4tI_sL_YBs0/https/i.imgur.com/Z1ALPb8.png")
    webhook.add_embed(embed)
    response = webhook.execute()

def ganesh(webhook_url, product_image, store, product, size, price, profile, date, time):
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title='Successful Checkout!', color=65280, url="https://twitter.com/TheGaneshBot")
    embed.set_thumbnail(url=product_image)
    embed.add_embed_field(name='Date Time', value='||'+date+' '+time+'||', inline=True)
    embed.add_embed_field(name='Store', value=store, inline=True)
    embed.add_embed_field(name='Profile', value='||'+profile+'||', inline=True)
    embed.add_embed_field(name='Product', value=product, inline=True)
    embed.add_embed_field(name='Size', value=size, inline=True)
    embed.add_embed_field(name='Price', value='$'+str(price)+'.00', inline=True)
    embed.add_embed_field(name='Order Number', value='||V'+str(random.randint(4000000000,5000000000))+'||', inline=False)
    embed.set_footer(text='@theGaneshBot • '+date, icon_url="https://images-ext-2.discordapp.net/external/XnfnaHmjhY6X2sMmA_z-5DoHnj5ZzpfudyBd2ABJ9h0/https/s3.eu-west-2.amazonaws.com/ganeshbotdl/ganesh_logo_square.png")
    webhook.add_embed(embed)
    response = webhook.execute()


def kodai_creation():
    webhook_url = input("Webhook: ")
    quantity = int(input("Number of Success: "))
    store = input("Store: ")
    group = input("Task Group Name: ")
    checkout_range_low = int(input("Checkout Speed Low End: "))
    checkout_range_high = int(input("Checkout Speed High End: "))
    product = input("Product: ")
    random_size = input("Random Sizing (Y/N): ")
    if random_size.lower() == "y":
        sizes = ["Random"]
    else:
        sizes = []
        addingSizes = True
        print("Enter Sizes - After Each Press Enter - When Finished Press Enter Again\n")
        while addingSizes == True:
            size = input()
            if size != "":
                sizes.append(size)
            else:
                addingSizes = False
    random_profile = input("List of Profiles (Y/N): ")
    profiles = []
    if random_profile.lower() == "n":
        profile = input("Profile: ")
        profiles.append(profile)
    else:
        addingProfiles = True
        print("Enter Profiles - After Each Press Enter - When Finished Press Enter Again\n")
        while addingProfiles == True:
            profile = input()
            if profile != "":
                profiles.append(profile)
            else:
                addingProfiles = False
    date = input("Date (Follow This Format - Sat Jul 11 2020): ")
    product_image = input("Product Image: ")
    i = 0
    while i < quantity:
        p1 = random.randint(checkout_range_low, checkout_range_high)
        p2 = random.randint(100,1000)
        checkout_speed = str(p1) + '.' + str(p2) + 's'
        size = random.choice(sizes)
        profile = random.choice(profiles)
        kodai(webhook_url, product_image, store, checkout_speed, product, size, profile, group, date)
        i += 1
        print("Sent")

def ganesh_creation():
    webhook_url = input("Webhook: ")
    quantity = int(input("Number of Success: "))
    date = input("Date (Format: 11/07/2020): ")
    time = input("Time (Format: 09:27:52): ")
    store = input("Store: ")
    profiles = []
    print("Enter Profiles - After Each Press Enter - When Finished Press Enter Again\n")
    addingProfiles = True
    while addingProfiles == True:
        profile = input()
        if profile != "":
            profiles.append(profile)
        else:
            addingProfiles = False
    product = input("Product: ")
    random_size = input("Random Sizing (Y/N): ")
    if random_size.lower() == "y":
        sizes = ["6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13"]
    else:
        sizes = []
        addingSizes = True
        print("Enter Sizes - After Each Press Enter - When Finished Press Enter Again\n")
        while addingSizes == True:
            size = input()
            if size != "":
                sizes.append(size)
            else:
                addingSizes = False
    price = int(input("Price (Only Give Int): "))
    product_image = input("Product Image: ")
    i = 0
    while i < quantity:
        size = random.choice(sizes)
        profile = random.choice(profiles)
        ganesh(webhook_url, product_image, store, product, size, price, profile, date, time)
        i += 1
        print("Sent")
    

def main():
    selection = int(input("""Pick the bot to simulate
1. Kodai
2. Ganesh
Selection: """))
    if selection == 1:
        kodai_creation()
    elif selection == 2:
        ganesh_creation()
    else:
        print("Invalid Selection")
    
main()