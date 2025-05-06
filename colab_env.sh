#!/bin/bash
# Clear Environment Setup Script for Google Colab

cyan='\033[1;36m'; yellow='\033[1;33m'; green='\033[1;32m'; red='\033[1;31m'; reset='\033[0m'

echo -e "${cyan}Cleaning up Colab environment...${reset}"

# 1️⃣ Remove RENDER environment variable from ~/.bashrc (and ~/.zshrc if it exists)
echo -e "${yellow}Removing environment variable RENDER...${reset}"
for shell_config in ~/.bashrc ~/.zshrc; do
  if [ -f "$shell_config" ]; then
    sed -i '/export RENDER="False"/d' "$shell_config"
  fi
done
# Also unset it for the current session
unset RENDER
echo -e "${green}✔ Environment variable RENDER removed successfully!${reset}"

# 2️⃣ Remove the virtual environment folder (if you created one under /content)
VENV_DIR="/content/macos_dev_env"
if [ -d "$VENV_DIR" ]; then
  echo -e "${yellow}Removing virtual environment ${VENV_DIR##*/}...${reset}"
  rm -rf "$VENV_DIR"
  echo -e "${green}✔ Virtual environment removed successfully!${reset}"
else
  echo -e "${red}⚠ Virtual environment not found. Skipping...${reset}"
fi

echo -e "${green}✅ Colab environment cleanup completed!${reset}"