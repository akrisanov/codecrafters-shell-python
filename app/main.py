from pathlib import Path
import os

BUILTINS = {"echo", "exit", "type"}


def main():
    while True:
        try:
            line = input("$ ")
        except EOFError:
            print()
            raise SystemExit

        command, args = parse(line)
        if not command:
            continue

        handle(command, args)


def parse(command: str) -> tuple[str | None, list[str]]:
    parts = command.split()
    if not parts:
        return None, []
    return parts[0], parts[1:]


def handle(command: str, args: list[str]):
    match command:
        case "type":
            if not args:
                print("type: missing argument")
                return
            handle_type(args[0])
        case "echo":
            print(*args)
        case "exit":
            raise SystemExit
        case _:
            print(f"{command}: command not found")


def handle_type(command: str):
    if command in BUILTINS:
        print(f"{command} is a shell builtin")
    elif result := find_exec(command):
        print(result)
    else:
        print(f"{command}: not found")


def find_exec(command: str) -> str | None:
    for dir in os.environ.get("PATH", "").split(os.pathsep):
        if not dir:
            continue

        candidate = Path(dir) / command

        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)

    return None


if __name__ == "__main__":
    main()
