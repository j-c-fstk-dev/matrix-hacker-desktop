# 🟢 Matrix Hacker Desktop
```
   ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗
   ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝
   ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝
   ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗
   ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗
   ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
```
[![GitHub](https://img.shields.io/badge/GitHub-j--c--fstk--dev%2Fmatrix--hacker--desktop-green?logo=github)](https://github.com/j-c-fstk-dev/matrix-hacker-desktop)
[![Stars](https://img.shields.io/github/stars/j-c-fstk-dev/matrix-hacker-desktop?style=social)](https://github.com/j-c-fstk-dev/matrix-hacker-desktop/stargazers)
![Platform](https://img.shields.io/badge/platform-Linux-blue)
![Shell](https://img.shields.io/badge/shell-bash-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Optimized](https://img.shields.io/badge/optimized-Core%202%20Duo+-brightgreen)

Transforme seu desktop Linux em uma **estação hacker Matrix**, otimizado para rodar até em um **Core 2 Duo**!

## 📋 O Que Este Projeto Faz?

Este é um setup completo de desktop Linux com:
- ✅ **Window Manager ultra-leve** (i3wm)
- ✅ **Efeito Matrix** (chuva de letras verde neon)
- ✅ **Monitor de sistema** em tempo real (CPU, RAM, Rede, Disco)
- ✅ **Terminal com painéis múltiplos** (tmux)
- ✅ **Widgets personalizados** (Polybar)
- ✅ **Tema verde Matrix** em tudo
- ✅ **Otimizado para PCs antigos**

## 🖥️ Requisitos Mínimos

- **CPU**: Core 2 Duo ou superior (qualquer dual-core de 2006+)
- **RAM**: 2GB (recomendado 4GB)
- **SO**: Kali Linux, Debian, Ubuntu, Arch, Fedora ou derivados
- **Espaço**: ~500MB para instalação

## 🚀 Instalação Rápida

### 1. Baixar o Projeto
```bash
# Clonar repositório
git clone https://github.com/SEU_USUARIO/matrix-hacker-desktop.git
cd matrix-hacker-desktop
```

### 2. Executar o Instalador
```bash
chmod +x install.sh
./install.sh
```

O instalador irá:
1. Detectar automaticamente sua distribuição Linux
2. Instalar todos os pacotes necessários
3. Configurar i3wm, polybar, rofi e picom
4. Fazer backup das suas configurações antigas
5. Aplicar o tema Matrix

### 3. Ativar

1. **Faça logout** da sua sessão atual
2. Na tela de login, selecione **"i3"** como ambiente de desktop
3. Faça login normalmente
4. Na primeira vez, o i3 perguntará sobre gerar um arquivo de config - escolha **Enter** (já temos nossa config)

## ⌨️ Atalhos de Teclado Principais

### Básicos
- `Super + Enter` - Abrir terminal
- `Super + D` - Launcher de aplicativos (Rofi)
- `Super + Shift + Q` - Fechar janela
- `Super + Shift + E` - Sair do i3
- `Super + Shift + R` - Reiniciar i3

> **Nota**: `Super` = Tecla Windows (⊞)

### Navegação
- `Super + H/J/K/L` ou `Setas` - Navegar entre janelas
- `Super + 1-9` - Mudar para workspace
- `Super + Shift + 1-9` - Mover janela para workspace

### Efeitos Matrix 🎬
- `Super + M` - **Matrix Rain** (cmatrix)
- `Super + Shift + H` - **Monitor de Sistema** (htop)
- `Super + N` - **Neofetch** (info do sistema)
- `Super + T` - **Dashboard Matrix** (nosso dashboard customizado)

### Layout de Janelas
- `Super + V` - Split vertical
- `Super + B` - Split horizontal
- `Super + F` - Fullscreen
- `Super + R` - Modo resize (depois use H/J/K/L para redimensionar)

## 📁 Estrutura do Projeto
```
matrix-hacker-desktop/
├── install.sh              # Instalador automático
├── config/                 # Configurações
│   ├── i3/                 # i3 window manager
│   │   └── config
│   ├── polybar/            # Barra superior
│   │   ├── config.ini
│   │   └── launch.sh
│   ├── rofi/               # Launcher
│   │   └── matrix.rasi
│   ├── picom/              # Compositor (transparências)
│   │   └── picom.conf
│   └── tmux.conf           # Terminal multiplexer
├── scripts/                # Scripts customizados
│   ├── matrix_dashboard.py # Dashboard em Python
│   └── matrix_wallpaper.sh # Wallpaper animado
└── README.md               # Este arquivo
```

## 🎨 Customização

### Mudar Cores

Edite `~/.config/i3/config`:
```bash
# Trocar verde (#00ff00) por outra cor
set $text-color #00ff00  # Mude para #ff0000 (vermelho), #0000ff (azul), etc.
```

### Adicionar Mais Efeitos

O i3 é totalmente customizável! Alguns exemplos:
```bash
# No arquivo ~/.config/i3/config, adicione:

# Abrir browser
bindsym $mod+b exec firefox

# Screenshot
bindsym Print exec scrot ~/Pictures/screenshot_%Y%m%d_%H%M%S.png

# Controle de volume
bindsym XF86AudioRaiseVolume exec amixer -q set Master 5%+
bindsym XF86AudioLowerVolume exec amixer -q set Master 5%-
```

### Configurar Tmux (Painéis)

Copie a configuração do tmux:
```bash
cp config/tmux.conf ~/.tmux.conf
tmux source-file ~/.tmux.conf
```

**Atalhos do Tmux**:
- `Ctrl+A` + `|` - Split vertical
- `Ctrl+A` + `-` - Split horizontal
- `Alt+H/J/K/L` - Navegar entre painéis (sem prefix!)
- `Ctrl+A` + `D` - Detach da sessão

### Adicionar Wallpaper Matrix Animado
```bash
# Edite ~/.config/i3/config e adicione no final:
exec_always --no-startup-id ~/.local/share/matrix-desktop/scripts/matrix_wallpaper.sh
```

**Nota**: Isso pode consumir mais recursos em PCs muito antigos!

## 🔧 Resolução de Problemas

### Polybar não aparece
```bash
# Reinicie o Polybar manualmente
~/.config/polybar/launch.sh
```

### Tela preta após login

1. Verifique se o i3 foi selecionado na tela de login
2. Tente pressionar `Super + Enter` para abrir um terminal
3. Se nada funcionar, faça Ctrl+Alt+F2, faça login no TTY e execute:
```bash
   cat ~/.xsession-errors  # Ver erros
```

### Python não encontrado
```bash
# Instalar Python 3
sudo apt install python3 python3-pip  # Debian/Ubuntu/Kali
sudo pacman -S python python-pip      # Arch
sudo dnf install python3 python3-pip  # Fedora
```

### Dashboard dá erro
```bash
# Instalar dependências Python
pip3 install --user psutil pyfiglet termcolor
```

### Muito lento no Core 2 Duo

Abra `~/.config/picom/picom.conf` e desabilite completamente o compositor:
```bash
# Comentar a linha exec_always no i3 config:
# exec_always --no-startup-id picom ...
```

## 📦 Componentes Incluídos

| Componente | Função | Leve? |
|------------|--------|-------|
| **i3wm** | Window manager tiling | ✅ Ultra |
| **Polybar** | Barra de status superior | ✅ Sim |
| **Rofi** | Launcher de apps | ✅ Sim |
| **Picom** | Compositor (transparências) | ⚠️ Moderado |
| **Tmux** | Multiplexer de terminal | ✅ Ultra |
| **cmatrix** | Efeito Matrix | ✅ Sim |
| **htop** | Monitor de processos | ✅ Sim |
| **Neofetch** | Info do sistema | ✅ Sim |

## 🎯 Próximos Passos

Depois de instalar, você pode:

1. **Explorar o i3**: Leia o [guia oficial](https://i3wm.org/docs/userguide.html)
2. **Customizar Polybar**: Veja [exemplos](https://github.com/polybar/polybar)
3. **Adicionar widgets**: Use [Conky](https://github.com/brndnmtthws/conky) ou [Eww](https://github.com/elkowar/eww)
4. **Criar scripts**: Adicione seus próprios scripts em `~/.local/share/matrix-desktop/scripts/`

## 🤝 Contribuindo

Melhorias são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

Algumas ideias:

- [ ] Adicionar mais temas de cores
- [ ] Criar instalador para outras distros (Gentoo, NixOS)
- [ ] Widget de criptomoedas
- [ ] Integração com ferramentas de hacking ético (nmap, metasploit)
- [ ] Dashboard web (acessível via browser)

## 📜 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

## ⚠️ Aviso

Este é um setup **estético e funcional**, não um sistema de segurança real. Use por sua conta e risco.

---

**Aproveite sua nova estação Matrix!** 🟢
```
Welcome to the Matrix, Neo...
```
