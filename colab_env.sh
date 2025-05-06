%%bash
#!/bin/bash
# Google Colab Setup Environment Script

cyan='\033[1;36m'; yellow='\033[1;33m'; green='\033[1;32m'; red='\033[1;31m'; reset='\033[0m'

echo -e "${cyan}Checking Google Colab Development Environment...${reset}"

# 1️⃣  Verify Python ≥ 3.10
PY_VERSION=$(python3 -c "import sys,platform; v=platform.python_version_tuple(); print('.'.join(v))")
if python3 - <<'PY' 2>/dev/null; then
import sys; major,minor,_ = sys.version_info[:3]
if (major, minor) < (3,10):
    sys.exit(1)
PY
then
  echo -e "${green}✔ Python ${PY_VERSION} detected (OK for Colab)${reset}"
else
  echo -e "${red}❌ Python < 3.10 detected.  Colab base images should already be ≥3.10.  Please restart the runtime.${reset}"
  exit 1
fi

# 2️⃣  Create a virtual environment (optional but keeps things isolated)
VENV_DIR="/content/colab_dev_env"
if [ ! -d "$VENV_DIR" ]; then
  echo -e "${yellow}Creating virtual environment ${VENV_DIR##*/}...${reset}"
  python3 -m venv "$VENV_DIR"
  echo -e "${green}✔ Virtual environment created!${reset}"
else
  echo -e "${yellow}Virtual environment already exists. Re‑using it.${reset}"
fi

# Activate it for the rest of this cell
source "$VENV_DIR/bin/activate"
echo -e "${green}✔ Virtual environment activated for this cell.${reset}"

# 3️⃣  Install dependencies (if requirements.txt is present in /content)
if [ -f "/content/requirements.txt" ]; then
  echo -e "${yellow}Installing packages from requirements.txt...${reset}"
  pip install --quiet --upgrade pip
  pip install --quiet -r /content/requirements.txt
  echo -e "${green}✔ All packages installed!${reset}"
else
  echo -e "${red}⚠ /content/requirements.txt not found — skipping pip install.${reset}"
fi

# 4️⃣  Set / unset the RENDER environment variable
echo -e "${yellow}Setting environment variable RENDER=False for this session...${reset}"
export RENDER="False"

for shell_config in ~/.bashrc ~/.zshrc; do
  if [ -f "$shell_config" ]; then
    # Remove any previous RENDER lines
    sed -i '/export RENDER="False"/d' "$shell_config"
    # Add it back so future !bash cells inherit it (optional)
    echo 'export RENDER="False"' >> "$shell_config"
  fi
done
echo -e "${green}✔ RENDER environment variable configured.${reset}"

echo -e "${green}✅ Colab environment setup completed!${reset}"