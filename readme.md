# ISDS Final Poject

## Python Environment Setup
1. Use a Virtual Environment (venv)
   + Install correct Python verson
   + Then, create a virtual environment in your project folder: `python3 -m venv group_project`
   + macOS/Linux: `source group_project/bin/activate`
   + Windows: `group_project\Script\activate`
2. Specify Python Version for the Project
   + Install pyenv
     + macOS: `brew install pyenv`
     + Windows: 
   + Configure pyenv:
    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
    source ~/.zshrc
    ```
   + Restart terminal  
   + Install python 3.12: `pyenv install 3.12.3`   
   + Check the python: `which python` 
   + Set it as local: `pyenv local 3.12.3` 
3. Use requirment.txt or pyproject.toml for Dependencies
   + Generate requirements.txt (for pip user) `pip freeze > requirements.txt`
   + Then, when someone else sets up the project, they just run: `pip install -r requirment.txt`  
## Topic 7 Develop Web App

### Adding new webpage
### Database setup



## Progress
- [ ] Research for the Python Web development Framework
- [ ] Adopte what UI Framework
- [ ] Setup development enironment 
- [ ] Understand the setting of MVT