from pathlib import Path
import os


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
    elif result := find_exec(command):
        print(result)
    else:
        print(f"{command}: not found")


def find_exec(command: str) -> str | None:
    path_env = os.environ.get("PATH", "")
    for dir in path_env.split(os.pathsep):
        if not dir:
            continue

        candidate = Path(dir) / command

        if candidate.exists() and candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)

    return None


if __name__ == "__main__":
    main()
