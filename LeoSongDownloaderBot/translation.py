from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} π

I'm Leo Song Downloader Bot π±π°

You can download any song within a shortime with this Bot π

If you want to know how to use this bot just
touch on " Help π "  Button π

Leo Projects π±π° 
"""    
    HELP_TEXT = """
Hello {}π

You should know following instructions to download songs π

You can download song by,

π°<code>/song <song name></code>: Download songs from all sources
Ex : <code>/song alone</code>

Or,

π° via youtube URL s... Send me any Youtube URL to download it π
"""
    ABOUT_TEXT = """
π° **Bot :** [Leo Song Downloader Bot π±π°](https://t.me/leosongdownloaderbot)
π° **Developer :** [Naviya π±π°](https://telegram.me/naviya2)
π° **Updates Channel :** [Leo Updates π±π°](https://telegram.me/new_ehi)
π° **Support Group :** [Leo Support π±π°](https://telegram.me/leosupportx)
π° **Language :** [Python3](https://python.org)
π° **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
π° **Server :** [VPS](https://www.digitalocean.com)
"""

    ABOUT_DEV_TEXT = """
<b>Developer is a Super Noob π

You can find him in telegram as @naviya2 π±π°

Developer's github account : [Github](https://github.com/Naviya2) π±π°

If you find any error on this bot please be kind to tell [Developer](https://t.me/naviya2) or in our [Support Group](https://t.me/leosupportx) π</b>
"""
    INFO_TEXT = """
Hey {mention},

Your details are here π

π° **First Name :** `{first_name}`
π° **Last Name  :** `{last_name}`
π° **Username   :** @{username}
π° **User Id    :** `{user_id}`
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Developerπ§βπ»', url='https://telegram.me/naviya2'),
        InlineKeyboardButton('Rate us β', url='https://t.me/tlgrmcbot?start=leosongdownloaderbot-review')
        ],[
        InlineKeyboardButton('Updates Channelπ£', url='https://t.me/new_ehi'),
        InlineKeyboardButton('Support Group π₯', url='https://t.me/leosupportx')
        ],[
        InlineKeyboardButton('Help π', callback_data='help')
        ],[
        InlineKeyboardButton('β Add me to your group β', url='t.me/leosongdownloaderbot?startgroup=true')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('About βοΈ', callback_data='about'),
        InlineKeyboardButton('User Info β', callback_data='info')
        ],[
        InlineKeyboardButton('Close β', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('Help π', callback_data='help'),
        InlineKeyboardButton('About Dev π§βπ»', callback_data='aboutdev')
        ],[
        InlineKeyboardButton('Close β', callback_data='close')
        ]]
    )
    INFO_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('About βοΈ', callback_data='about'),
        InlineKeyboardButton('Help π', callback_data='help')
        ],[
        InlineKeyboardButton('Close β', callback_data='close')
        ]]
    )
    ABOUT_DEV_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home π ', callback_data='home'),
        InlineKeyboardButton('Help π', callback_data='help'),
        InlineKeyboardButton('About βοΈ', callback_data='about')
        ],[
        InlineKeyboardButton('Close β', callback_data='close')
        ]]
    ) 
