def main():
    while True:
        command, args = prepare(input("$ "))
        handle(command, args)


def prepare(command: str) -> tuple[str, list[str]]:
    parts = command.split()
    return parts[0], parts[1:]


def handle(command: str, args: list[str]):
    if command == "exit":
        exit()
    elif command == "echo":
        print(*args)
    else:
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
