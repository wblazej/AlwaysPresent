# AlwaysPresent
Bot for quick and comfortable checking presence on online lessons on Discord.

The bot uses polish database called PESEL for converting Discord servers nicks to names and surnames. That helps to sort them alphabetically which is easy to check presence quickly. <br>
Example: from `19. Błażej Wrzosok Kl. 2c` to `Wrzosok Błażej`

## Usage
**Requirements** <br>
Docker (latest version) <br>
Linux based OS
### Setting up
```
git clone https://github.com/wblazej/AlwaysPresent
cd AlwaysPresent
echo "TOKEN=<your_bot_token>" > .env
docker build -t alwayspresent .
docker run -d -t alwayspresent
```

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

## Technologies
Language **Python v3.8** <br>
Running on **Docker v20.10.3** <br>
Library **discord.py v1.5.1**

## Introduction
![bot_introduction](https://user-images.githubusercontent.com/62674438/111455335-f508f500-8715-11eb-8b1e-75f527b663d0.png)
