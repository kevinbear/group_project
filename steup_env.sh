#!/bin/bash
# macOS/Linux Setup Environment Script

echo -e "\033[1;36mChecking macOS/Linux Development Environment...\033[0m"

# Check Homebrew Installation
if command -v brew &>/dev/null; then
    echo -e "\033[1;32m✔ Homebrew is installed: $(brew --version | head -n 1)\033[0m"
else
    echo -e "\033[1;31m❌ Homebrew is not installed. Installing now...\033[0m"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Check Python Installation
if command -v python3 &>/dev/null; then
    echo -e "\033[1;32m✔ Python is installed: $(python3 --version)\033[0m"
else
    echo -e "\033[1;31m❌ Python is not installed. Installing now...\033[0m"
    brew install python
fi

# Check pip Installation
if command -v pip3 &>/dev/null; then
    echo -e "\033[1;32m✔ pip is installed: $(pip3 --version)\033[0m"
else
    echo -e "\033[1;31m❌ pip is not installed. Installing now...\033[0m"
    python3 -m ensurepip --default-pip
fi

# Check pyenv Installation
if command -v pyenv &>/dev/null; then
    echo -e "\033[1;32m✔ pyenv is installed: $(pyenv --version)\033[0m"
else
    echo -e "\033[1;31m❌ pyenv is not installed. Installing now...\033[0m"
    brew install pyenv
    echo -e "\033[1;33mAdding pyenv to shell configuration...\033[0m"
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
    source ~/.zshrc
fi

# Create Virtual Environment
echo -e "\033[1;36mCreating virtual environment (macos_dev_env)...\033[0m"
python3 -m venv macos_dev_env
echo -e "\033[1;32m✔ Virtual environment created: macos_dev_env\033[0m"

# Activate Virtual Environment
echo -e "\033[1;33mTo activate the virtual environment, run:\033[0m"
echo -e "\033[1;37msource macos_dev_env/bin/activate\033[0m"

# Install Required Packages
echo -e "\033[1;36mInstalling dependencies from requirements.txt...\033[0m"
pip3 install -r requirements.txt
echo -e "\033[1;32m✔ All required packages installed!\033[0m"

echo -e "\033[1;32m✅ macOS/Linux environment setup completed!\033[0m"
