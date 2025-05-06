%%bash
#!/bin/bash
# Google Colab Setup Environment Script  (fixed)

cyan='\033[1;36m'; yellow='\033[1;33m'; green='\033[1;32m'; red='\033[1;31m'; reset='\033[0m'

echo -e "${cyan}Checking Google Colab Development Environment...${reset}"

# 1️⃣  Verify Python ≥ 3.10
if python3 - <<'PY' 2>/dev/null
import sys, os
sys.exit(0) if sys.version_info >= (3,10) else sys.exit(1)
PY
then
  PY_VERSION=$(python3 -c "import platform; print(platform.python_version())")
  echo -e "${green}✔ Python ${PY_VERSION} detected (OK for Colab)${reset}"
else
  echo -e "${red}❌ Python < 3.10 detected. Colab runtimes should already be ≥3.10. Please restart the runtime.${reset}"
  exit 1
fi

# 2️⃣  Create / activate virtual environment inside the project folder
#     (Uses 'virtualenv' so we avoid ensurepip issues)
VENV_DIR="$PWD/.venv"         # << change the folder name if you prefer

if [ ! -d "$VENV_DIR" ]; then
  echo -e "${yellow}Creating virtual environment at ${VENV_DIR}...${reset}"
  # Ensure virtualenv is available (brings its own pip)
  pip install --quiet --upgrade pip virtualenv
  virtualenv "$VENV_DIR"
  echo -e "${green}✔ Virtual environment created!${reset}"
else
  echo -e "${yellow}Virtual environment already exists. Re‑using it.${reset}"
fi

# Activate it for the rest of the current cell
source "$VENV_DIR/bin/activate"
echo -e "${green}✔ Virtual environment activated for this cell.${reset}"

# 3️⃣  Install dependencies (if requirements.txt exists in the current directory)
REQ_FILE="$PWD/requirements.txt"     # <‑‑ Was /content/requirements.txt

if [ -f "$REQ_FILE" ]; then
  echo -e "${yellow}Installing packages from $(basename "$REQ_FILE")...${reset}"
  pip install --quiet --upgrade pip
  pip install --quiet -r "$REQ_FILE"
  echo -e "${green}✔ All packages installed!${reset}"
else
  echo -e "${red}⚠ requirements.txt not found in $(pwd) — skipping pip install.${reset}"
fi

# 4️⃣  Set RENDER=False for this session and future !bash cells
echo -e "${yellow}Setting environment variable RENDER=False...${reset}"
export RENDER="False"
for shell_config in ~/.bashrc ~/.zshrc; do
  if [ -f "$shell_config" ]; then
    sed -i '/export RENDER="False"/d' "$shell_config"
    echo 'export RENDER="False"' >> "$shell_config"
  fi
done
echo -e "${green}✔ RENDER environment variable configured.${reset}"

echo -e "${green}✅ Colab environment setup completed!${reset}"