import dataclasses

import pytest

from src.constants import Commands
from src.directories import DirectoriesManager, Directory


@pytest.fixture(scope="function")
def directories_manager():
    directories_manager = DirectoriesManager()
    directories_manager.directory.add(Directory("dir_1"))
    directories_manager.directory.add(Directory("dir_2"))
    directories_manager.directory.folders.get("dir_1").add(Directory("dir_3"))
    return directories_manager


class TestDirectoriesManager:
    def test_create_command(self, directories_manager):
        directories_manager.create("dir_4")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {
                                   "folders": {},
                                   "name": "dir_3"}},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       },
                       "dir_4": {
                           "folders": {},
                           "name": "dir_4"
                       }
                   },
                   "name": ""
               }

    def test_create_command__child_dir(self, directories_manager):
        directories_manager.create("dir_1/dir_3/dir_4")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {
                                   "folders": {
                                       "dir_4": {
                                           "folders": {},
                                           "name": "dir_4"
                                       }
                                   },
                                   "name": "dir_3"}},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_create_command__already_exist(self, directories_manager):
        directories_manager.create("dir_1")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {"folders": {}, "name": "dir_3"}},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_delete_command(self, directories_manager):
        directories_manager.delete("dir_1")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_delete_command__child_dir(self, directories_manager):
        directories_manager.delete("dir_1/dir_3")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_delete_command__non_exist(self, directories_manager):
        directories_manager.delete("dir_4")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {"folders": {}, "name": "dir_3"}},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_move_command(self, directories_manager):
        directories_manager.move("dir_2", "dir_1")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {"folders": {}, "name": "dir_3"},
                               "dir_2": {"folders": {}, "name": "dir_2"}
                           },
                           "name": "dir_1"
                       }
                   },
                   "name": ""
               }

    def test_move_command__with_subdir(self, directories_manager):
        directories_manager.move("dir_1", "dir_2")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_2": {
                           "folders": {
                               "dir_1": {
                                   "folders": {
                                       "dir_3": {"folders": {}, "name": "dir_3"}},
                                   "name": "dir_1"
                               },
                           },
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_move_command__non_valid_source_dir(self, directories_manager):
        directories_manager.move("dir_1/dir_4", "dir_2")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {"folders": {}, "name": "dir_3"}},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_move_command__non_valid_dest_dir(self, directories_manager):
        directories_manager.move("dir_1/dir_3", "dir_4")
        assert dataclasses.asdict(directories_manager.directory) == \
               {
                   "folders": {
                       "dir_1": {
                           "folders": {
                               "dir_3": {"folders": {}, "name": "dir_3"}},
                           "name": "dir_1"
                       },
                       "dir_2": {
                           "folders": {},
                           "name": "dir_2"
                       }
                   },
                   "name": ""
               }

    def test_list_command(self, directories_manager):
        try:
            directories_manager.list()
        except Exception as exc:
            pytest.fail(f"Error during executing {Commands.LIST.value}: {exc}")
