## AlwaysPresent
### Introduction
A bot for a quick and comfortable presence verification on online lessons on Discord. Everything you have to do is just run a simple command and your students have to register thir presence by reacting on the message sent by the bot.

The bot uses polish a database called PESEL for converting Discord servers nicks to names and surnames. That helps to sort them alphabetically which helps to check presence quickly.

Example: from `15. Jan Nowak Kl. 4D` to `Jan Nowak`

### Setup
#### Run the bot
```
git clone https://github.com/wblazej/AlwaysPresent
cd AlwaysPresent
echo "TOKEN=your_bot_token" > .env
sudo docker build -t always-present-bot .
sudo docker run -d -t --name always-present-bot --restart=always always-present-bot
```
When the bot is ready, run `&help` command on discord channel to see list of commands. If you don't know how to setup discord application and get a token, see [discord docs](https://discord.com/developers/docs/intro)


#### Stop the bot
```
sudo docker stop always-present-bot
```

### Others

#### Discord API wrapper
https://github.com/Rapptz/discord.py

This library is not supported any more :(

#### Discord docs
https://discord.com/developers/docs/intro
