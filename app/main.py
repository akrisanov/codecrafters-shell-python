def main():
    while True:
        command, args = parse(input("$ "))
        handle(command, args)


def parse(command: str) -> tuple[str, list[str]]:
    parts = command.split()
    return parts[0], parts[1:]


def handle(command: str, args: list[str]):
    match command:
        case "type":
            handle_type(args[0])
        case "echo":
            print(*args)
        case "exit":
            raise SystemExit
        case _:
            print(f"{command}: command not found")


def handle_type(command: str):
    if command in ("echo", "exit", "type"):
        print(f"{command} is a shell builtin")
    else:
        print(f"{command}: not found")


if __name__ == "__main__":
    main()
