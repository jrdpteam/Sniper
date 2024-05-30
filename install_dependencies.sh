#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo -e "\e[91mPlease run this script with sudo privileges.\e[0m"
    exit
fi

function check_python_module() {
    python3 -c "import $1" &>/dev/null
}

function install_python_module() {
    echo "Installing $1..."
    python3 -m pip install $1
}

if ! check_python_module "colorama"; then
    install_python_module "colorama"
else
    echo "Colorama is already installed."
fi

if ! check_python_module "scapy"; then
    install_python_module "scapy"
else
    echo "Scapy is already installed."
fi

if ! check_python_module "urllib.parse"; then
    install_python_module "urllib3"
else
    echo "Urllib is already installed."
fi

if ! command -v zenity &>/dev/null; then
    echo "Installing zenity..."
    sudo apt update
    sudo apt install -y zenity
else
    echo "Zenity is already installed."
fi
