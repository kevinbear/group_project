#!/bin/bash
# Clear Environment Setup Script

echo -e "\033[1;36mCleaning up development environment...\033[0m"

# Remove RENDER environment variable from shell configurations
echo -e "\033[1;33mRemoving environment variable RENDER...\033[0m"
for shell_config in ~/.bashrc ~/.zshrc; do
    sed -i '' '/export RENDER="False"/d' "$shell_config" 2>/dev/null || sed -i '/export RENDER="False"/d' "$shell_config"
done
echo -e "\033[1;32m✔ Environment variable RENDER removed successfully!\033[0m"

# Remove virtual environment
if [ -d "$HOME/macos_dev_env" ]; then
    echo -e "\033[1;33mRemoving virtual environment macos_dev_env...\033[0m"
    rm -rf "$HOME/macos_dev_env"
    echo -e "\033[1;32m✔ Virtual environment removed successfully!\033[0m"
else
    echo -e "\033[1;31m⚠ Virtual environment not found. Skipping...\033[0m"
fi

# Apply changes
source ~/.zshrc 2>/dev/null || source ~/.bashrc 2>/dev/null

echo -e "\033[1;32m✅ Environment cleanup completed!\033[0m"