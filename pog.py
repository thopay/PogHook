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
    embed = DiscordEmbed(title='New Login!')
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

bogosLinks = {
    "Purple":"https://images-ext-1.discordapp.net/external/0snL6kY84EzAlzBZYctQ28Fmfc8Mno7INEkUkt8kdms/https/assets.supremenewyork.com/194641/sm/EZRewR7le4k.jpg",
    "Heather Grey":"https://images-ext-2.discordapp.net/external/aeLakKwpVo198psXLeeIKrhkNDJLJ7uiNgTnfODSXzA/https/assets.supremenewyork.com/194629/sm/tDcdFhfvf8I.jpg",
    "Black":"https://images-ext-1.discordapp.net/external/lm7rTD-hOm-VNgXYpJjHg18qqNIxsi4MfM-WAFq8diY/https/assets.supremenewyork.com/194645/sm/iiGbsIkjF5Q.jpg",
    "Light Olive":"https://images-ext-1.discordapp.net/external/N5pBDpGRaBnxuYreTus8a3nFmh7PDm9gAb7PqHpC0as/https/assets.supremenewyork.com/194627/sm/ZjwB8HAlKzA.jpg",
    "Navy":"https://images-ext-1.discordapp.net/external/vVzeHks-F0TBfE1Is5GnbPCVMX22kKZ2FF87-I4C5-4/https/assets.supremenewyork.com/194637/sm/6A-a1TK1zQs.jpg",
    "Lemon":"https://images-ext-2.discordapp.net/external/1PK2G4Mr6VLdLoBumxgPguwqyYcTexPdXj8cI24TwKQ/https/assets.supremenewyork.com/194635/sm/SH6fdgu042c.jpg",
    "Red":"https://images-ext-1.discordapp.net/external/_4QU4eimSR_FvIxROOchjaHs78CEs_0QG23wg9GO2kI/https/assets.supremenewyork.com/194633/sm/7IAx2BS99LU.jpg"
}

def mek(webhook_url, product, size, color, profile, email):
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(description='Successful Checkout! :white_check_mark:', color=5152773)
    embed.set_thumbnail(url=bogosLinks[color.title()])
    embed.add_embed_field(name='Product', value=product, inline=True)
    embed.add_embed_field(name='Size/Color', value=size+'/'+color, inline=True)
    embed.add_embed_field(name='订单号(order#)', value='||'+str(random.randint(125000000,125900000))+'||', inline=True)
    embed.add_embed_field(name='ProfileName', value='||'+profile+'||', inline=True)
    embed.add_embed_field(name='ProfileName', value='||'+email+'||', inline=True)
    embed.add_embed_field(name='Checkout IP', value='||localhost||', inline=True)
    embed.add_embed_field(name='App Version', value='0.7.2', inline=True)
    embed.add_embed_field(name='模式(mode)', value='api', inline=True)
    embed.add_embed_field(name='Checkout Speed', value=str(random.randint(8,20))+'.'+str(random.randint(100,800))+'s', inline=True)
    embed.add_embed_field(name='Checkout Delay', value='0ms', inline=True)
    embed.add_embed_field(name='Queued', value='True', inline=True)
    embed.add_embed_field(name='Dropped Time', value='2020-12-03T16:00:'+str(random.randint(12,19))+'.'+str(random.randint(100,900))+'Z', inline=True)
    embed.add_embed_field(name='CaptchaBypass', value='False', inline=True)
    embed.add_embed_field(name='ThreeDBypass', value='True', inline=True)
    embed.add_embed_field(name='CCA', value='False', inline=True)
    embed.add_embed_field(name='TicketMode', value='True', inline=True)
    embed.add_embed_field(name='ProfileBypass', value='True', inline=True)
    embed.add_embed_field(name='Status', value='paid', inline=True)
    embed.set_footer(text='2020-12-03T16:0'+str(random.randint(0,2))+':'+str(random.randint(10,59))+'.'+str(random.randint(100,900))+'Z', icon_url="https://images-ext-2.discordapp.net/external/zgUG44I9dqW193Y6_Vv7aMrJ92DO4gCy5VVd9u9cpXg/http/icons.iconarchive.com/icons/iconscity/flags/256/usa-icon.png")
    webhook.add_embed(embed)
    response = webhook.execute()
    while int(response.status_code) == 429:
        time.sleep(3)
        response = webhook.execute()

def mek_creation():
    webhook_url = input("Webhook: ")
    product = input("Product: ")
    quantity = int(input("Number of Success: "))
    profiles = []
    print("Enter Profiles - After Each Press Enter - When Finished Press Enter Again\n")
    addingProfiles = True
    while addingProfiles == True:
        profile = input()
        if profile != "":
            profiles.append(profile)
        else:
            addingProfiles = False
    sizes = ["Small","Medium","Large","XLarge"]
    email = input("Email: ")
    i = 0
    while i < quantity:
        size = random.choice(sizes)
        profile = random.choice(profiles)
        color = random.choice(["Purple","Heather Grey","Black","Light Olive", "Navy","Lemon","Red"])
        mek(webhook_url, product, size, color, profile, email)
        i += 1
        print("Sent")


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
3. Mek
Selection: """))
    if selection == 1:
        kodai_creation()
    elif selection == 2:
        ganesh_creation()
    elif selection == 3:
        mek_creation()
    else:
        print("Invalid Selection")
    
main()