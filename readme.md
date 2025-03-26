# ISDS Final Poject

## Python Environment Setup

1. Use a Virtual Environment (venv)
   - Install correct Python verson
   - Then, create a virtual environment in your project folder: `python3 -m venv group_project`
   - macOS/Linux: `source group_project/bin/activate`
   - Windows: `group_project\Script\activate`
2. Specify Python Version for the Project
   - Install pyenv
     - macOS: `brew install pyenv`
     - Windows:
   - Configure pyenv:
   ```bash
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   source ~/.zshrc
   ```
   - Restart terminal
   - Install python 3.12: `pyenv install 3.12.3`
   - Check the python: `which python`
   - Set it as local: `pyenv local 3.12.3`
3. Use requirment.txt or pyproject.toml for Dependencies
   - Generate requirements.txt (for pip user) `pip freeze > requirements.txt`
   - Then, when someone else sets up the project, they just run: `pip install -r requirment.txt`

## UI Design

[Figma Workspace](https://www.figma.com/design/576Wocaf7E4dsJbYljJaso/Restaurant-Web-App?node-id=0-1&t=nmuGb90mpe9oR6oa-1)

## Topic 7 Develop Web App

For our final group project, we are developing a restaurant web
application using Python and the Django web framework. Our goal is to
create a dynamic and interactive website that goes beyond a simple
online menu. The web app will feature multiple tabs, including a
homepage, separate sections for breakfast, lunch, and dinner menus,
and an online ordering page.

## Progress

- [x] Research for the Python Web development Framework
- [x] Adopt Boostrap 5 UI Framework
- [x] Setup development enironment
- [x] Base HTML template
- [x] Finish About HTML
