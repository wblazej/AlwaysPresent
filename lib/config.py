class Config:
    PREFIX  = "&"
    VERSION = "2.0"
    INVITE  = "https://discord.com/api/oauth2/authorize?client_id=776565552289153024&permissions=486464&scope=bot"

    # Links
    WEBSITE   = "http://presence.ddns.net"
    DOCS_PATH = "/docs"

    # Colors
    ERROR_COLOR = 0xc72222
    MAIN_COLOR  = 0x0bb556

    # Commands descriptions
    HELP_COMMAND_DESCRIPTION   = "pokazuje listę komend"
    INVITE_COMMAND_DESCRIPTION = "wysyła zaproszenie bota na serwer"

    # Commands arguments descriptions
    HELP_ARGUMENT_DESCRIPTION = "pokazuje pomoc do komendy"

    # Icons urls
    INFO_ICON = "https://i.imgur.com/TVS0605.png"

    # Translations
    TRANSLATION_DESCRIPTION = "Opis"
    TRANSLATION_ALIASES     = "Alternatywne nazwy"
    TRANSLATION_ARGUMENTS   = "Argumenty"

    # Messages
    UNKNOWN_COMMAND     = f"Nieprawidłowa komenda. Wpisz **{PREFIX}help**"
    MISSING_PERMISSIONS = "Brak uprawnień do tej komendy"
    SERVER_COMMAND      = "Tę komendę można wykonywać jedynie na serwerze"
    WRONG_CONFIG        = f'Błąd w konfiguracji roli bota na serwerze. Bot nie ma permisji do wykonania jakieś czynności, która jest niezbędna do poprawnego działania. Zobacz dokumenctację na {WEBSITE}{DOCS_PATH}'
    HELP_INFO           = "Wpisz nazwę komendy z argumentem `--help`, aby dowiedzieć się więcej o komendzie"