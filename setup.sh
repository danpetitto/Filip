#!/bin/bash

echo "🚀 FLL Fitness Web - Setup Script"
echo "=================================="

# Kontrola Python verze
echo "📋 Kontroluji Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 není nainstalován!"
    exit 1
fi

python_version=$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1,2)
echo "✅ Python $python_version je k dispozici"

# Vytvoření virtuálního prostředí
echo "🔧 Vytvářím virtuální prostředí..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtuální prostředí vytvořeno"
else
    echo "⚠️  Virtuální prostředí už existuje"
fi

# Aktivace virtuálního prostředí
echo "🔄 Aktivuji virtuální prostředí..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Aktualizuji pip..."
pip install --upgrade pip

# Instalace závislostí
echo "📦 Instaluji závislosti..."
pip install -r requirements.txt

# Vytvoření složky templates pokud neexistuje
echo "📁 Vytvářím potřebné složky..."
mkdir -p templates
mkdir -p static/css
mkdir -p static/js
mkdir -p static/images

echo "✅ Setup dokončen!"
echo ""
echo "🎯 Pro spuštění aplikace:"
echo "   1. Aktivuj virtuální prostředí: source venv/bin/activate"
echo "   2. Spusť aplikaci: python web.py"
echo "   3. Otevři v prohlížeči: http://localhost:5000"
echo ""
echo "🛠️  Pro deaktivaci virtuálního prostředí: deactivate"
echo ""

# Volitelné automatické spuštění
read -p "Chceš spustit aplikaci hned? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Spouštím Flask aplikaci..."
    python web.py
fi