# ISDS Final Poject
## Python Environment Setup

### Prerequisites
- Ensure you have Python installed (version 3.8 or higher recommended).
- Install necessary dependencies as outlined in `requirements.txt`.

### Step 1: Download and Extract the Setup Files
1. Download the setup files from the provided 
   [Project Download Link](https://www.dropbox.com/home/Yin-Bo%20Kuo/2025%20Spring/ISDS%20558%20Advance%20Software%20Development%20Web%20Application/group%207%20final%20project/Source%20Code)
2. Extract the downloaded ZIP file to your desired location.

### Step 2: Open in VS Code and Terminal
1. Open Visual Studio Code.
2. Navigate to **File > Open Folder** and select the extracted folder.
3. Open the integrated terminal in VS Code by clicking **Terminal > New Terminal** or using the shortcut:
   - Windows: `Ctrl + ~`
   - macOS/Linux: `Cmd + ~`

### Step 3: Run the Environment Setup Script
#### Windows (PowerShell)
1. In the VS Code terminal or PowerShell, navigate to the extracted folder.
2. Execute the following command:
   ```powershell
   .\setup_env.ps1
   ```

#### macOS/Linux (Bash)
1. In the VS Code terminal or a system terminal, navigate to the extracted folder.
2. Give the permission to run the script:
   ```bash
   chmod +x setup_env.sh
   ```
2. Run the following command:
   ```bash
   ./setup_env.sh
   ```

This will set up the virtual environment and install required dependencies from `requirements.txt`.

### Step 5: Start the Django Server
Once the environment is set up, navigate to the project folder and start the server.

#### Windows
```powershell
cd final_project
python manage.py runserver
```

#### macOS/Linux
```bash
cd final_project
python manage.py runserver
```

The server should now be running, and you can access your application in a web browser at:
```
http://127.0.0.1:8000/restaurant/home
```

### Troubleshooting
#### 1. Ensure you have the necessary permissions to execute scripts.
- If dependencies fail to install, try manually running:
  ```bash
  pip install -r requirements.txt
  ```
- If the server does not start, check for missing migrations and apply them:
  ```bash
  python manage.py migrate
  ```
#### 2. `Step 3` possible errors:
   + Encoding Error in PowerShell. If you run `.\setup_env.ps1` and encounter the following issue, you need to change the `.\setup_env.ps1` encoding to `utf8bom`
   ```powershell
   At C:\Users\<yourname>\group_project\setup_env.ps1:55 char:1
   + }
   + ~
   Unexpected token '}' in expression or statement.
   At C:\Users\<yourname>\group_project\setup_env.ps1:77 char:1
   + }
   + ~
   Unexpected token '}' in expression or statement.
   At C:\Users\<yourname>\group_project\setup_env.ps1:127 char:1
   + }
   + ~
   Unexpected token '}' in expression or statement.
   At C:\Users\<yourname>\group_project\setup_env.ps1:146 char:1
   + }
   + ~
   Unexpected token '}' in expression or statement.
      + CategoryInfo          : ParserError: (:) [], ParseException
      + FullyQualifiedErrorId : UnexpectedToken

   ```

   + If you see this error`pyenv-win installation failed. Please install manually from https://github.com/pyenv-win/pyenv-win`, just close your VS code and reopen it.
---

## Develop Web App (Topic 7)
For our final group project, we are developing a restaurant web
application using Python and the Django web framework. Our goal is to
create a dynamic and interactive website that goes beyond a simple
online menu. The web app will feature multiple tabs, including a
homepage, separate sections for breakfast, lunch, and dinner menus,
and an online ordering page.

## Group Member
+ Kevin Kuo, Creator
+ Erin Vallejo, Orator
+ Hannah Nguyen, Interpreter
+ Mohammand Siddique Khan, Deliverer
+ Akash Yarehalli Satis, Orator

## UI Design

[Figma Workspace](https://www.figma.com/design/576Wocaf7E4dsJbYljJaso/Restaurant-Web-App?node-id=0-1&t=nmuGb90mpe9oR6oa-1)

## Progress

- [x] Research for the Python Web development Framework
- [x] Adopt Boostrap 5 UI Framework
- [x] Setup development enironment
- [x] Base HTML template
