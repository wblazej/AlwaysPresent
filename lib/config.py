class Config:
    PREFIX = "&"
    VERSION = "2.0"

    # Links
    WEBSITE = "http://presence.ddns.net"
    DOCS_PATH = "/docs"

    # Colors
    ERROR_COLOR = 0xc72222

    # Messages
    UNKNOWN_COMMAND = f"Nieprawidłowa komenda. Wpisz **{PREFIX}help**"
    MISSING_PERMISSIONS = "Brak uprawnień do tej komendy"
    SERVER_COMMAND = "Tę komendę można wykonywać jedynie na serwerze"
    WRONG_CONFIG = f'Błąd w konfiguracji roli bota na serwerze. Bot nie ma permisji do wykonania jakieś czynności, która jest niezbędna do poprawnego działania. Zobacz dokumenctację na {WEBSITE}{DOCS_PATH}'