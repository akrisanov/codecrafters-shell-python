def main():
    while True:
        command = input("$ ")
        if command == "exit":
            exit()
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
