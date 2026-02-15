#!/bin/bash

# Matrix Wallpaper Rain Effect
# Cria uma chuva Matrix como wallpaper usando xterm

# Matar instâncias anteriores
killall -q matrix_wallpaper.sh 2>/dev/null

# Obter tamanho da tela
SCREEN_WIDTH=$(xdpyinfo | awk '/dimensions/{print $2}' | cut -d 'x' -f1)
SCREEN_HEIGHT=$(xdpyinfo | awk '/dimensions/{print $2}' | cut -d 'x' -f2)

# Criar múltiplas janelas de cmatrix como wallpaper
for i in {1..3}; do
    xterm -geometry ${SCREEN_WIDTH}x${SCREEN_HEIGHT}+0+0 \
          -bg black \
          -fg green \
          -fa 'Monospace' \
          -fs 10 \
          +sb \
          -override \
          -e "cmatrix -abs -C green -u 5" &
    
    sleep 0.5
done

# Enviar janelas para o fundo (simular wallpaper)
sleep 2
for win in $(wmctrl -l | grep cmatrix | awk '{print $1}'); do
    wmctrl -i -r $win -b add,below,sticky
    wmctrl -i -r $win -b add,skip_taskbar,skip_pager
done
