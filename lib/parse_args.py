def parse_args(args: tuple) -> dict:
    args = list(args)
    parsed = {}

    for i in range(len(args)):
        if args[i].startswith('-') or args[i].startswith('--'):
            parsed[args[i].replace('-', '')] = {"arg": True}
            if i + 1 < len(args):
                if not args[i + 1].startswith('-') and not args[i + 1].startswith('--'):
                    parsed[args[i].replace('-', '')]['value'] = args[i + 1]
                    i += 1

    return parsed