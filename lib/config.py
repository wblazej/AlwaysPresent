import discord

class Config:
    # General
    PREFIX                          = "&"
    VERSION                         = "2.0"
    INVITATION                      = "https://discord.com/api/oauth2/authorize?client_id=776565552289153024&permissions=486464&scope=bot"
    LANGUAGE                        = "Python v3.8"
    LIBRARY                         = f"dicord.py v{discord.__version__}"
    REPO                            = "https://github.com/wblazej/AlwaysPresent"
    RUNNING_ON                      = "Docker v20.10.3"
    AUTHOR                          = "Błażej Wrzosok"
    ICONS_AUTHOR                    = "https://icons8.com"
    TIMEZONE                        = "Europe/Warsaw"

    # Colors
    ERROR_COLOR                     = 0xc72222
    MAIN_COLOR                      = 0x432bcc

    # Commands descriptions
    HELP_COMMAND_DESCRIPTION        = "pokazuje listę komend"
    INVITATION_COMMAND_DESCRIPTION  = "wysyła zaproszenie bota na serwer"
    QUESTION_COMMAND_DESCRIPTION    = "tworzy ankietę z wynikami na żywo. Pytanie i odpowiedzi zapisz w cudzysłowiu"
    LESSON_COMMAND_DESCRIPTION      = "rozpoczyna lekcję na kanale tekstowym"
    PERMISSIONS_COMMAND_DESCRIPTION = "wyświetla uprawnienia, jakie bot powinien posiadać"
    BOT_COMMAND_DESCRIPTION         = "pokazuje informacje o bocie"

    # Commands arguments descriptions
    HELP_ARGUMENT_DESCRIPTION       = "pokazuje pomoc do komendy"
    QUESTION_ARGUMENT_DESCRIPTION   = "pytanie w ankiecie"
    ANSWER_ARGUMENT_DESCRIPTION     = "odpowiedź do ankiety"
    TIME_ARGUMENT_DESCRIPTION       = "przez ile czasu w minutach można zaznaczyć obecność"
    PRACTICE_ARGUMENT_DESCRIPION    = "zmienia lekcję na praktykę"
    NO_MENTION_ARG_DESCRIPTION      = "wysyła infomację o lekcji bez pingu `@here`"

    # Commands usage examples
    QUESTION_COMMAND_EXAMPLE        = f"{PREFIX}question -q \"Tak czy nie?\" -a1 \"Tak\" -a2 \"Nie\""
    LESSON_COMMAND_EXAMPLE          = f"{PREFIX}lesson -t 60"

    # Icons urls
    HELP_ICON                       = "https://imgur.com/cvBXTLC.png"
    INVITATION_ICON                 = "https://imgur.com/vfgmyFA.png"
    PERMISSIONS_ICON                = "https://imgur.com/YhfUFIS.png"
    QUESTION_ICON                   = "https://imgur.com/QzypOcB.png"
    LESSON_ICON                     = "https://imgur.com/y0GQT1k.png"
    BOT_ICON                        = "https://imgur.com/iHhNdyD.png"

    # Translations
    TRANSLATION_DESCRIPTION         = "Opis"
    TRANSLATION_ALIASES             = "Alternatywne nazwy"
    TRANSLATION_ARGUMENTS           = "Argumenty"
    TRANSLATION_INVITATION          = "Zaproszenie"
    TRANSLATION_EXAMPLE             = "Przykład użycia"
    TRANSLATION_PERMISSIONS         = "Uprawnienia bota"
    TRANSLATION_PERMISSIONS_CODE    = "Kod uprawnień"
    TRANSLATION_LESSON              = "Lekcja"
    TRANSLATION_PRACTICE            = "Praktyka"
    TRANSLATION_TEACHER             = "Nauczyciel"
    TRANSLATION_LEADER              = "Prowadzący"
    TRANSLATION_STARTED             = "Rozpoczęto"
    TRANSLATION_LESSON_END          = "Koniec lekcji"
    TRANSLATION_PRESENCE_LIST       = "Lista obecności"
    TRANSLATION_BOT_INFO            = "Informacje o bocie"
    TRANSLATION_LANGUAGE            = "Język"
    TRANSLATION_LIBRARY             = "Biblioteka"
    TRNASLATION_VERSION             = "Wersja"
    TRANSLATION_REPOSITORY          = "Repozytorium"
    TRANSLATION_RUNNING_ON          = "Uruchomiony na"
    TRANSLATION_AUTHOR              = "Autor"
    TRANSLATION_ICONS               = "Ikony"

    # Messages
    UNKNOWN_COMMAND                 = f"Nieprawidłowa komenda. Wpisz **{PREFIX}help**"
    MISSING_PERMISSIONS             = "Brak uprawnień do tej komendy"
    SERVER_COMMAND                  = "Tę komendę można wykonywać jedynie na serwerze"
    WRONG_CONFIG                    = f'Bot nie ma permisji do wykonania jakieś czynności, która jest niezbędna do poprawnego działania. Wpisz **{PREFIX}permissions**, aby otrzymać listę wymaganych uprawnień'
    HELP_INFO                       = "Wpisz nazwę komendy z argumentem `--help`, aby dowiedzieć się więcej o komendzie"
    NO_QUESTION                     = "Pytanie nie zostało podane"
    TWO_ANSWERS_REQUIRED            = "Pytanie musi zawierać conajmniej dwie odpowiedzi"
    MAX_NINE_ANSWERS                = "Pytanie może mieć maksymalnie 9 odpowiedzi"
    CHOOSE_ANSWER                   = "\nWybierz odpowiedź, klikając w reakcję"
    TIME_INTEGER_REQIURED           = "Czas powinien być liczbą całkowitą podaną w minutach"
    LESSON_PRESENCE_INFORMATION     = "Kliknij reakcję poniżej, aby wpisać się na listę obecności"
    BOT_DESCRIPTION                  = "Bot do szybkiego i wygodnego sprawdzania obecności na lekcjach online, prowadzonych na Discordzie"

    # Emojis
    PRESENCE_EMOJI                  = "👋"
    DISCORD_EMOJIS_NUMBERS          = [
        ':one:',
        ':two:',
        ':three:',
        ':four:',
        ':five:',
        ':six:',
        ':seven:',
        ':eight:',
        ':nine:'
    ]
    DISCORD_EMOJIS_NUMBERS_UNICODE  = [
        '\U00000031\U000020E3',
        '\U00000032\U000020E3',
        '\U00000033\U000020E3',
        '\U00000034\U000020E3',
        '\U00000035\U000020E3',
        '\U00000036\U000020E3',
        '\U00000037\U000020E3',
        '\U00000038\U000020E3',
        '\U00000039\U000020E3'
    ]

    # Permissions
    PERMISSIONS_CODE                = 486464
    PERMISSIONS_LIST                = [
        "Czytanie wiadomości",
        "Wysyłanie wiadomości",
        "Zarządzanie wiadomościami",
        "Zamieszczanie linków",
        "Czytanie historii wiadomości",
        "Wspominanie `@here`",
        "Używanie zewnętrznych emoji",
        "Dodawanie reakcji",
        "Wyświetlanie kanałów"
    ]

    # Date formating
    DAYS_OF_WEEK                    = {
        0: "poniedziałek",
        1: "wtorek",
        2: "środa",
        3: "czwartek",
        4: "piątek",
        5: "sobota",
        6: "niedziela"
    }
    MONTHS                          = {
        1: "stycznia",
        2: "lutego",
        3: "marca",
        4: "kwietnia",
        5: "maja",
        6: "czerwca",
        7: "lipca",
        8: "sierpnia",
        9: "września",
        10: "października",
        11: "listopada",
        12: "grudnia"
    }