import os
import shutils
from pathlib import Path
import glob

def remove_unused_adapters():
    adapters = glob.glob("../ref/adapters/*.fa")
    for fa in adapters:
        if '{{ cookiecutter.clip_file }}' != Path(fa).name:
            os.remove(fa)

def remove_unused_notebooks():
    notebooks = glob.glob("../notebooks/*.ipynb")
    for nb in notebooks:
        if '{{ cookiecutter.analysis_type }}' not in Path(nb).name:
            os.remove(nb)


def main():
    remove_unused_adapters()
    remove_unused_notebooks()

if __name__ == 'main':
    main()
