from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to ** @whisper_king_bot **

I am the Master of Whisperers (like Varys in Game of Thrones).

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

To see how to use me press 'How to Use' below.

**Powered By: @attitude_galaxy**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="✨Go Back✨", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒Send a Whisper🔑", switch_inline_query="")
        ],
        [
            InlineKeyboardButton(",🥂How to use🥂", callback_data="help"),
            InlineKeyboardButton("🧪About🧪", callback_data="about")
        ],
        [InlineKeyboardButton("⚡More Cool Bots⚡", url="https://t.me/attitude_galaxy")],
        [InlineKeyboardButton("🔊Support Group🔊", url="https://t.me/Sweetkingdom1")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@WhisperStarkBot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @attitude_galaxy

Source Code : [🔥🥂Click Here⚡🔐](https://github.com/ItsAttitudeking/whisper_king_bot)

Inspired By : nnbbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @alone_shaurya_king
    """
