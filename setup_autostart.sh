#!/bin/bash
mkdir -p ~/.config/autostart
cat <<EOF > ~/.config/autostart/dynamic-wallpaper.desktop
[Desktop Entry]
Type=Application
Name=Dynamic Wallpaper
Exec=sh -c 'DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus DISPLAY=:0 python3 /home/thiago_dev/dynamic-wallpaper/dynamic_wallpaper.py'
Icon=wallpaper
Terminal=false
EOF
echo "Arquivo de autostart criado em ~/.config/autostart/dynamic-wallpaper.desktop"
