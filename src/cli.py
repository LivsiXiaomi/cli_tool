

def read_command_file(filepath: str) -> str:
    try:
        for line in open(filepath, "r"):
            yield line.rstrip()
    except FileNotFoundError as exc:
        print("Error during processing...")
        print(exc)


if __name__ == '__main__':
    commands = read_command_file("test_input.txt")
    for command in commands:
        print(command)
