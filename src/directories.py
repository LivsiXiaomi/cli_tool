from dataclasses import dataclass
from typing import Dict

from src.constants import Commands


@dataclass
class Directory:
    name: str
    folders: Dict = None

    def __post_init__(self):
        self.folders = dict()

    def add(self, child_directory: 'Directory') -> bool:
        self.folders[child_directory.name] = child_directory
        return True

    def pop(self, child_directory: 'Directory') -> 'Directory':
        folder = self.folders.pop(child_directory.name, None)
        return folder


@dataclass
class DirectoriesManager:
    directory: Directory = None

    def __post_init__(self):
        self.directory = Directory("")

    def _depth_walk(self, directory: Directory, shift: int) -> None:
        print("".join([" "*shift, directory.name]))
        for key, elem in directory.folders.items():
            self._depth_walk(elem, shift + 1)
        return None

    def _check_if_folders_exists(self, folder_path: str) -> str:
        folder_path_elems = folder_path.split("/")
        non_exist_folder = ''
        folder = self.directory
        for elem in folder_path_elems:
            if elem in folder.folders.keys():
                folder = folder.folders[elem]
            else:
                non_exist_folder = elem
        return non_exist_folder

    def _get_directory(self, folder_path: str) -> Directory:
        folder_path_elems = folder_path.split("/")
        current_directory = self.directory
        for elem in folder_path_elems:
            if elem in current_directory.folders:
                current_directory = current_directory.folders.get(elem)
        return current_directory

    def _add_directories(self, folder_path: str) -> None:
        folder_path_elems = folder_path.split("/")
        parent_folder = self.directory
        for elem in folder_path_elems:
            new_folder = Directory(elem)
            if parent_folder:
                parent_folder.add(new_folder)
            parent_folder = new_folder

    def _pop_directories(self, folder_path: str) -> 'Directory':
        folder_path_elems = folder_path.split("/")
        folder = self.directory
        for elem in folder_path_elems[0:-1]:
            folder = folder.folders.get(elem)
        return folder.pop(folder.folders[folder_path_elems[-1]])

    def create(self, folder_path: str) -> None:
        print(f"{Commands.CREATE.value} {folder_path}")
        non_exist_folder = self._check_if_folders_exists(folder_path)
        if not non_exist_folder:
            print(f"Cannot create {folder_path} - {non_exist_folder} already exist")
            return None
        self._add_directories(folder_path)

    def delete(self, folder_path: str) -> None:
        print(f"{Commands.DELETE.value} {folder_path}")
        non_exist_folder = self._check_if_folders_exists(folder_path)
        if non_exist_folder:
            print(f"Cannot delete {folder_path} - {non_exist_folder} does not exist")
            return None
        self._pop_directories(folder_path)

    def move(self, source_folder: str, dest_folder: str) -> None:
        print(f"{Commands.MOVE.value} {source_folder} {dest_folder}")
        non_exist_folder = self._check_if_folders_exists(source_folder)
        if non_exist_folder:
            print(f"Cannot move {source_folder} - {non_exist_folder} does not exist")
            return None
        non_exist_folder = self._check_if_folders_exists(dest_folder)
        if non_exist_folder:
            print(f"Cannot move to {dest_folder} - {non_exist_folder} does not exist")
            return None
        moved_directory = self._pop_directories(source_folder)
        root_directory = self._get_directory(dest_folder)
        root_directory.add(moved_directory)

    def list(self) -> None:
        print(Commands.LIST.value)
        for _, elem in self.directory.folders.items():
            self._depth_walk(elem, 0)
