class Config:
    PREFIX                          = "&"
    VERSION                         = "2.0"
    INVITATION                      = "https://discord.com/api/oauth2/authorize?client_id=776565552289153024&permissions=486464&scope=bot"

    # Links
    WEBSITE                         = "http://presence.ddns.net"
    DOCUMENTATION                   = f"{WEBSITE}/docs"

    # Colors
    ERROR_COLOR                     = 0xc72222
    MAIN_COLOR                      = 0x0bb556

    # Commands descriptions
    HELP_COMMAND_DESCRIPTION        = "pokazuje listę komend"
    INVITATION_COMMAND_DESCRIPTION  = "wysyła zaproszenie bota na serwer"
    QUESTION_COMMAND_DESCRIPTION    = "tworzy ankietę z wynikami na żywo. Pytanie i odpowiedzi zapisz w cudzysłowiu"

    # Commands arguments descriptions
    HELP_ARGUMENT_DESCRIPTION       = "pokazuje pomoc do komendy"
    QUESTION_ARGUMENT_DESCRIPTION   = "pytanie w ankiecie"
    ANSWER_ARGUMENT_DESCRIPTION     = "odpowiedź do ankiety"

    # Commands usage examples
    QUESTION_COMMAND_EXAMPLE        = f"{PREFIX}question -q \"Tak czy nie?\" -a1 \"Tak\" -a2 \"Nie\""

    # Icons urls
    INFO_ICON                       = "https://i.imgur.com/TVS0605.png"
    INVITATION_ICON                 = "https://imgur.com/oqJl0QT.png"

    # Translations
    TRANSLATION_DESCRIPTION         = "Opis"
    TRANSLATION_ALIASES             = "Alternatywne nazwy"
    TRANSLATION_ARGUMENTS           = "Argumenty"
    TRANSLATION_INVITATION          = "Zaproszenie"
    TRANSLATION_EXAMPLE             = "Przykład użycia"

    # Messages
    UNKNOWN_COMMAND                 = f"Nieprawidłowa komenda. Wpisz **{PREFIX}help**"
    MISSING_PERMISSIONS             = "Brak uprawnień do tej komendy"
    SERVER_COMMAND                  = "Tę komendę można wykonywać jedynie na serwerze"
    WRONG_CONFIG                    = f'Błąd w konfiguracji roli bota na serwerze. Bot nie ma permisji do wykonania jakieś czynności, która jest niezbędna do poprawnego działania. Zobacz dokumenctację na {DOCUMENTATION}'
    HELP_INFO                       = "Wpisz nazwę komendy z argumentem `--help`, aby dowiedzieć się więcej o komendzie"
    NO_QUESTION                     = "Pytnie nie zostało podane"
    TWO_ANSWERS_REQUIRED            = "Pytanie musi zawierać conajmniej dwie odpowiedzi"
    MAX_NINE_ANSWERS                = "Pytanie może mieć maksymalnie 9 odpowiedzi"
    CHOOSE_ANSWER                   = "\nWybierz odpowiedź, klikając w reakcję"