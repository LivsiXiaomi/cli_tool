import argparse
import logging

from src.constants import Commands, ERROR_MESSAGE_TEMPLATE
from src.directories import DirectoriesManager


def _read_file(filepath: str) -> str:
    try:
        for line in open(filepath, "r"):
            yield line.rstrip()
    except FileNotFoundError as exc:
        logging.error(exc)


def cli(file_path: str) -> None:
    command_manager = DirectoriesManager()
    commands = _read_file(file_path)
    for command in commands:
        command_args = command.split(" ")
        if command_args[0] == Commands.CREATE.value:
            if len(command_args) != 2:
                print(ERROR_MESSAGE_TEMPLATE.format("create"))
                continue
            command_manager.create(command_args[1])
        elif command_args[0] == Commands.DELETE.value:
            if len(command_args) != 2:
                print(ERROR_MESSAGE_TEMPLATE.format("delete"))
                continue
            command_manager.delete(command_args[1])
        elif command_args[0] == Commands.MOVE.value:
            if len(command_args) != 3:
                print(ERROR_MESSAGE_TEMPLATE.format("move"))
                continue
            command_manager.move(command_args[1], command_args[2])
        elif command_args[0] == Commands.LIST.value:
            command_manager.list()
        else:
            print("Unsupported command. Move to the next command...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, help="path to file with commands")
    args = parser.parse_args()
    cli(args.input_file)
