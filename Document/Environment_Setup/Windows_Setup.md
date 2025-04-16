# Windows Setup Development Environment

## 1. Download the Zip File from Dropbox Folder

Download the source code from the Dropbox folder. Ensure you have the correct access and permissions to download the file.
[Project Download Link](https://www.dropbox.com/scl/fi/g6k40whssmres4yc8zs6e/group_project-main.zip?rlkey=8kztrjbwyor04722pk7mkuhk7&e=1&st=bwxlthbm&dl=0)

## 2. Place the Project Zip File in an Empty Folder

Move the project zip file to a dedicated directory of your choice.

## 3. Unzip the Project

Unzip the downloaded `group_project-main.zip` file into your chosen directory. Ensure the extracted folder contains all necessary project files.

## 4. Open the Terminal (PowerShell) and Navigate to the Folder

### Using PowerShell:

```ps1
cd <path_to_project_folder>
```

### Using VS Code:

- Open VS Code.
- Go to `File > Open Folder`.
- Select the project directory.

## 5. Ensure Python is Installed on Your Computer

### Install Python:

- Download Python from the [official Python website](https://www.python.org/downloads/).
- During installation, ensure the option **"Add Python to PATH"** is selected.

### Verify Python Installation:

```ps1
py --version
```

This should return the installed version of Python (e.g., `Python 3.x.x`). If it does not, restart your system and try again.

### Verify pip Installation:

```ps1
pip list
```

If the command doesn’t work, follow these steps to add Python and pip to the system PATH:

1. Open the **Start Menu** and search for "Environment Variables".
2. Click on **Edit the system environment variables**.
3. In the **System Properties** window, click **Environment Variables**.
4. Under **System Variables**, find and select `Path`, then click **Edit**.
5. Click **New** and add the following paths:
   - `C:\Users\<your_user>\AppData\Local\Programs\Python\Python3X\`
   - `C:\Users\<your_user>\AppData\Local\Programs\Python\Python3X\Scripts\`
6. Click **OK** to save changes and close all windows.
7. Restart your computer or reopen PowerShell and verify the installation:
   ```ps1
   pip --version
   ```

## 6. Install `pyenv-win`
Run the following command:

```powershell
Get-ExecutionPolicy
```

If it returns `Restricted`, it means scripts are not allowed to run.

### Temporarily Allow Scripts (Recommended)

To allow running scripts just for this session, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This allows scripts to run only for the current session.

### Permanently Allow Scripts (If Needed)

If you want to change the execution policy permanently, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```


### Install `pyenv-win` in PowerShell:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

- Restart PowerShell (or close and reopen VS Code).
- Check if `pyenv-win` is installed:
  ```powershell
  pyenv --version
  ```

### Install Python Version Using `pyenv-win`

- List available Python versions:
  ```powershell
  pyenv install -l
  ```
- Install Python 3.12 (or your preferred version):
  ```powershell
  pyenv install 3.12
  ```
- Set Python 3.12 as the global version:
  ```powershell
  pyenv global 3.12
  ```
- Verify the Python version:
  ```powershell
  pyenv version
  python -c "import sys; print(sys.executable)"
  ```

## 7. Create a Virtual Environment

### Navigate to Your Project Directory:

```powershell
cd <path_to_project_folder>
```

### Create a Virtual Environment:

```powershell
py -m venv windows_dev_env
```

Ensure that the `windows_dev_env` folder is created inside your project directory.

## 8. Activate the Virtual Environment

### Run the following command in PowerShell:

```powershell
.\windows_dev_env\Scripts\Activate.ps1
```

If you encounter an execution policy error, run the following command first:
```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```
Then, try activating the virtual environment again.

Once activated, you should see `(windows_dev_env)` at the beginning of your terminal prompt.

## 9. Install the Required Packages

With the virtual environment activated, install the dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

If you encounter errors during installation, ensure that `requirements.txt` is present in the project folder and that your internet connection is stable.

## 10. Run the Django Project

### Navigate to the Project Directory:

Ensure you are in the correct project folder where `manage.py` is located:

```powershell
cd <your_project_path>\group_project\final_project
```

### Apply Migrations:

Run the following command to apply any pending migrations:

```powershell
python manage.py migrate
```

Follow the prompts to set up a username, email, and password.

### Run the Development Server:

Start the Django development server:

```powershell
python manage.py runserver
```

### Access the Project:

Once the server is running, open your browser and navigate to:

```
http://127.0.0.1:8000/restaurant/home
```

If you want to login admin panel, you can log into:
```
http://127.0.0.1:8000/admin
```
### Admin Panel Login:
Email: your school email  
Password: project7
### Stop the server
Press `ctrl + c` in the terminal can stop the server

## 11. Deactivate the Virtual Environment

Once you're done, deactivate the virtual environment:

```powershell
deactivate
```

If you plan to work again, reactivate the virtual environment before running any Python commands.


