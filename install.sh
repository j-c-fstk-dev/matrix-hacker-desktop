#!/bin/bash

# Matrix Hacker Desktop - Instalador Universal
# Compatível com Debian/Ubuntu/Kali, Arch, Fedora
# Otimizado para hardware antigo (Core 2 Duo+)

set -e

GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗       ║
║   ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝       ║
║   ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝        ║
║   ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗        ║
║   ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗       ║
║   ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝       ║
║                                                           ║
║            HACKER DESKTOP - INSTALADOR v1.0              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Detectar distribuição
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo -e "${RED}Não foi possível detectar a distribuição${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Detectado: $PRETTY_NAME${NC}"
echo ""

# Função de instalação baseada na distro
install_packages() {
    case $DISTRO in
        kali|debian|ubuntu)
            echo -e "${CYAN}[*] Atualizando repositórios...${NC}"
            sudo apt-get update
            
            echo -e "${CYAN}[*] Instalando pacotes base...${NC}"
            sudo apt-get install -y \
                i3-wm i3status i3lock \
                polybar \
                rofi \
                feh \
                picom \
                tmux \
                cmatrix \
                htop \
                neofetch \
                python3 \
                python3-pip \
                fonts-font-awesome \
                fonts-powerline \
                xterm \
                rxvt-unicode \
                alacritty || echo "Alacritty não disponível, usando alternativas"
            ;;
        
        arch|manjaro)
            echo -e "${CYAN}[*] Instalando via pacman...${NC}"
            sudo pacman -Syu --noconfirm
            sudo pacman -S --noconfirm \
                i3-wm i3status i3lock \
                polybar \
                rofi \
                feh \
                picom \
                tmux \
                cmatrix \
                htop \
                neofetch \
                python \
                python-pip \
                ttf-font-awesome \
                powerline-fonts \
                xterm \
                rxvt-unicode \
                alacritty
            ;;
        
        fedora)
            echo -e "${CYAN}[*] Instalando via dnf...${NC}"
            sudo dnf install -y \
                i3 i3status i3lock \
                polybar \
                rofi \
                feh \
                picom \
                tmux \
                cmatrix \
                htop \
                neofetch \
                python3 \
                python3-pip \
                fontawesome-fonts \
                powerline-fonts \
                xterm \
                rxvt-unicode \
                alacritty
            ;;
        
        *)
            echo -e "${RED}Distribuição não suportada: $DISTRO${NC}"
            echo "Tente instalar manualmente: i3-wm, polybar, rofi, feh, picom, tmux, cmatrix, htop"
            exit 1
            ;;
    esac
}

# Instalar dependências Python
install_python_deps() {
    echo -e "${CYAN}[*] Instalando dependências Python...${NC}"
    pip3 install --user psutil pyfiglet termcolor || \
    python3 -m pip install --user psutil pyfiglet termcolor
}

# Criar diretórios de configuração
setup_dirs() {
    echo -e "${CYAN}[*] Criando diretórios de configuração...${NC}"
    mkdir -p ~/.config/{i3,polybar,rofi,picom}
    mkdir -p ~/.local/share/matrix-desktop/{scripts,wallpapers}
    mkdir -p ~/Pictures/wallpapers
}

# Backup de configurações existentes
backup_configs() {
    echo -e "${CYAN}[*] Fazendo backup de configurações existentes...${NC}"
    timestamp=$(date +%Y%m%d_%H%M%S)
    
    [ -f ~/.config/i3/config ] && cp ~/.config/i3/config ~/.config/i3/config.backup_$timestamp
    [ -f ~/.config/polybar/config.ini ] && cp ~/.config/polybar/config.ini ~/.config/polybar/config.ini.backup_$timestamp
}

# Copiar configurações
copy_configs() {
    echo -e "${CYAN}[*] Copiando configurações Matrix...${NC}"
    
    # Copiar configs do diretório atual
    if [ -d "config" ]; then
        cp -r config/i3/* ~/.config/i3/ 2>/dev/null || true
        cp -r config/polybar/* ~/.config/polybar/ 2>/dev/null || true
        cp -r config/rofi/* ~/.config/rofi/ 2>/dev/null || true
        cp -r config/picom/* ~/.config/picom/ 2>/dev/null || true
    fi
    
    # Copiar scripts
    if [ -d "scripts" ]; then
        cp -r scripts/* ~/.local/share/matrix-desktop/scripts/
        chmod +x ~/.local/share/matrix-desktop/scripts/*.sh 2>/dev/null || true
        chmod +x ~/.local/share/matrix-desktop/scripts/*.py 2>/dev/null || true
    fi
    
    # Copiar wallpapers
    if [ -d "assets/wallpapers" ]; then
        cp -r assets/wallpapers/* ~/Pictures/wallpapers/ 2>/dev/null || true
    fi
}

# Configurar autostart
setup_autostart() {
    echo -e "${CYAN}[*] Configurando autostart...${NC}"
    
    # Adicionar ao .xinitrc ou .xsession
    if [ ! -f ~/.xinitrc ]; then
        echo "exec i3" > ~/.xinitrc
    fi
}

# Menu de instalação
echo -e "${GREEN}Escolha o tipo de instalação:${NC}"
echo "1) Instalação completa (recomendado)"
echo "2) Apenas configurações (pacotes já instalados)"
echo "3) Cancelar"
echo ""
read -p "Opção [1]: " choice
choice=${choice:-1}

case $choice in
    1)
        echo -e "${GREEN}==> Iniciando instalação completa...${NC}"
        install_packages
        install_python_deps
        setup_dirs
        backup_configs
        copy_configs
        setup_autostart
        ;;
    2)
        echo -e "${GREEN}==> Instalando apenas configurações...${NC}"
        setup_dirs
        backup_configs
        copy_configs
        setup_autostart
        ;;
    3)
        echo "Instalação cancelada."
        exit 0
        ;;
    *)
        echo -e "${RED}Opção inválida${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}║  ✓ INSTALAÇÃO CONCLUÍDA COM SUCESSO!                     ║${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}║  Para ativar:                                             ║${NC}"
echo -e "${GREEN}║  1. Faça logout                                           ║${NC}"
echo -e "${GREEN}║  2. Selecione 'i3' na tela de login                      ║${NC}"
echo -e "${GREEN}║  3. Use Super+Enter para abrir terminal                  ║${NC}"
echo -e "${GREEN}║  4. Use Super+D para launcher de apps                    ║${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}║  Atalhos Matrix:                                          ║${NC}"
echo -e "${GREEN}║  • Super+M = Matrix Rain (cmatrix)                       ║${NC}"
echo -e "${GREEN}║  • Super+H = Monitor de Sistema (htop)                   ║${NC}"
echo -e "${GREEN}║  • Super+N = Neofetch                                     ║${NC}"
echo -e "${GREEN}║  • Super+T = Dashboard Matrix                             ║${NC}"
echo -e "${GREEN}║                                                           ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Deseja reiniciar agora? [s/N]${NC}"
read -p "" restart
if [[ $restart =~ ^[Ss]$ ]]; then
    sudo reboot
fi
