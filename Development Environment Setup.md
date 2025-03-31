# Development Environment Setup (Windows & macOS)

## 1. Download the Zip File from Dropbox Folder

Download the source code from the Dropbox folder. Ensure you have the correct access and permissions to download the file.  
[Project Download Link](https://www.dropbox.com/home/Yin-Bo%20Kuo/2025%20Spring/ISDS%20558%20Advance%20Software%20Development%20Web%20Application/group%207%20final%20project/Source%20Code)

## 2. Place the Project Zip File in an Empty Folder

Move the project zip file to a dedicated directory of your choice.

## 3. Unzip the Project

Extract the downloaded `group_project-main.zip` file into your chosen directory. Ensure the extracted folder contains all necessary project files.

## 4. Open the Terminal and Navigate to the Folder

### Windows (PowerShell):
```powershell
cd <path_to_project_folder>
```

### macOS (Terminal):
```sh
cd <path_to_project_folder>
```

### Using VS Code:
- Open VS Code.
- Go to `File > Open Folder`.
- Select the project directory.

## 5. Ensure Python is Installed on Your Computer

### Install Python:
- Download Python from the [official Python website](https://www.python.org/downloads/).
- During installation (Windows), ensure the option **"Add Python to PATH"** is selected.

### Verify Python Installation:
#### Windows:
```powershell
py --version
```
#### macOS:
```sh
python3 --version
```

### Verify pip Installation:
#### Windows:
```powershell
pip list
```
#### macOS:
```sh
pip3 list
```

## 6. Install `pyenv`
### Windows (`pyenv-win`)
Run the following command in PowerShell:
```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
Restart PowerShell and verify installation:
```powershell
pyenv --version
```

### macOS (`pyenv`)
```sh
brew install pyenv
```
Add the following to `~/.zshrc`:
```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
source ~/.zshrc
```
Verify installation:
```sh
pyenv --version
```

### Install Python Using `pyenv`
#### Windows:
```powershell
pyenv install 3.12
pyenv global 3.12
```
#### macOS:
```sh
pyenv install 3.12
pyenv global 3.12
```
Verify:
```sh
pyenv version
python3 -c "import sys; print(sys.executable)"
```

## 7. Create a Virtual Environment
#### Windows:
```powershell
py -m venv windows_dev_env
```
#### macOS:
```sh
python3 -m venv mac_dev_env
```

## 8. Activate the Virtual Environment
#### Windows:
```powershell
.\windows_dev_env\Scripts\Activate.ps1
```
If you encounter an execution policy error:
```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

#### macOS:
```sh
source mac_dev_env/bin/activate
```

Once activated, you should see the virtual environment name in the terminal prompt.

## 9. Install the Required Packages
Ensure the virtual environment is activated, then run:
#### Windows:
```powershell
pip install -r requirements.txt
```
#### macOS:
```sh
pip3 install -r requirements.txt
```

## 10. Run the Django Project
Ensure you are in the project folder where `manage.py` is located:
```sh
cd <your_project_path>/group_project/final_project
```

### Apply Migrations:
```sh
python3 manage.py migrate
```

### Run the Development Server:
```sh
python3 manage.py runserver
```

### Access the Project:
```
http://127.0.0.1:8000/restaurant/home
```

### Admin Panel Login:
```
http://127.0.0.1:8000/admin
```
- **Email:** your school email  
- **Password:** project7  

### Stop the Server:
Press `Ctrl + C` in the terminal.

## 11. Deactivate the Virtual Environment
#### Windows:
```powershell
deactivate
```
#### macOS:
```sh
deactivate
```

