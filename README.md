# AlwaysPresent
Bot for quick and comfortable checking presence on online lessons on Discord. Everything you have to do is just run a simple command and your students have to check off them presence by reacting on message sent by the bot.

The bot uses polish database called PESEL for converting Discord servers nicks to names and surnames. That helps to sort them alphabetically which is easy to check presence quickly.

Example: from `19. Błażej Wrzosok Kl. 2c` to `Wrzosok Błażej`

## Setup on docker
### Running
```
git clone https://github.com/wblazej/AlwaysPresent
cd AlwaysPresent
echo "TOKEN=<your_bot_token>" > .env
docker build -t alwayspresent .
docker run -d -t alwayspresent
```
If you don't know how to setup discord application and get a token, see [discord docs](https://discord.com/developers/docs/intro)


### Getting logs
```
docker ps --all | grep alwayspresent
docker logs <container_id>
```

### Stop process
```
docker ps | grep alwayspresent
docker stop <container_id>

# or

docker ps | grep alwayspresent
docker kill <container_id> # not recommended
```

#### Library
https://github.com/Rapptz/discord.py

#### Discord docs
https://discord.com/developers/docs/intro
