#!/usr/bin/env python
import os
from pathlib import Path


if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        os.remove(Path.cwd() / "LICENSE")
