#!/usr/bin/env bash

# Encerrar instâncias existentes do polybar
killall -q polybar

# Aguardar até que os processos sejam encerrados
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Lançar polybar
echo "---" | tee -a /tmp/polybar.log
polybar matrix 2>&1 | tee -a /tmp/polybar.log & disown

echo "Polybar lançado..."
