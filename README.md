<!-- Papel de Parede Dinâmico -->

<p align="center">
  <img src="https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/logo.png">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Mantido%3F-Sim-green?style=for-the-badge">
  <img src="https://img.shields.io/github/license/adi1090x/dynamic-wallpaper?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/adi1090x/dynamic-wallpaper?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/adi1090x/dynamic-wallpaper?color=violet&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/adi1090x/dynamic-wallpaper?color=teal&style=for-the-badge">
</p>

<p align="center">Um script <code>bash</code> simples para definir papéis de parede de acordo com a hora atual, usando o <b>agendador de tarefas cron</b>.</p>

![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/main.gif) <br />

### Visão Geral

+ 25+[(mais)](https://github.com/adi1090x/files/tree/master/dynamic-wallpaper/wallpapers) tipos diferentes de conjuntos de papéis de parede (HD/UHD/4K/5K).
+ Suporte a `pywal` adicionado.
+ Usuários podem adicionar seus próprios papéis de parede.
+ Com o `Cron`, o papel de parede muda de acordo com a hora, ao longo do dia.
+ Testado em:
  - **`Gerenciadores de Janelas`**: Funciona em todos os gerenciadores de janelas (testado em todos os WMs que o Archcraft possui)
  - **`Compositores Wayland`**: `sway`, `wayfire`, `river`, `newm`, `hyprland`
  - **`Ambientes de Desktop`**: `KDE`, `Pantheon`, `Gnome`, `Deepin`, `Cinnamon`, `XFCE`, `LXDE`, `MATE`, `Zorin`, `Budgie`

### Dependências

Instale os seguintes programas no seu sistema antes de usar o `dwall` -

- **`feh`**: Para definir papéis de parede em WMs
- **`cron`**: Para agendar uma tarefa para o dwall
- **`xrandr`**: Apenas se você estiver usando o desktop XFCE
- **`pywal`**: para suporte ao pywal (opcional)

Instale `feh`, `cron` e `xrandr` -
```bash
# No Archlinux
$ sudo pacman -Sy xorg-xrandr feh cronie

# No Ubuntu ou Debian
$ sudo apt-get install x11-xserver-utils feh cron
```

> Para suporte ao swaywm, os usuários devem instalar o [oguri](https://github.com/vilhalmer/oguri). O daemon `oguri` deve ser iniciado para que o script funcione. O `Oguri` pode ser instalado no Arch Linux via [AUR](https://aur.archlinux.org/packages/oguri-git/).

### Instalação

Siga os passos abaixo para instalar o `dwall` no seu sistema -
> Você pode executar o `test.sh` para testá-lo antes de instalar no seu sistema.

+ Clone este repositório -
```
$ git clone https://github.com/adi1090x/dynamic-wallpaper.git
```

+ Mude para o diretório clonado e execute `install.sh` -
```
$ cd dynamic-wallpaper
$ chmod +x install.sh
$ ./install.sh
```

### Execute o programa

+ Abra o terminal e execute `dwall` -
```
$ dwall

╺┳┓╻ ╻┏┓╻┏━┓┏┳┓╻┏━╸   ╻ ╻┏━┓╻  ╻  ┏━┓┏━┓┏━┓┏━╸┏━┓
 ┃┃┗┳┛┃┗┫┣━┫┃┃┃┃┃     ┃╻┃┣━┫┃  ┃  ┣━┛┣━┫┣━┛┣╸ ┣┳┛
╺┻┛ ╹ ╹ ╹╹ ╹╹ ╹╹┗━╸   ┗┻┛╹ ╹┗━╸┗━╸╹  ╹ ╹╹  ┗━╸╹┗╸

Dwall V3.0   : Define papéis de parede de acordo com a hora atual.
Desenvolvido por : Aditya Shakya (@adi1090x)

Uso : test.sh [-h] [-p] [-s estilo]

Opções:
   -h	  Mostra esta mensagem de ajuda
   -p	  Usa o pywal para definir o papel de parede
   -s	  Nome do estilo a ser aplicado
   
Estilos disponíveis:  aurora  beach  bitday  chihuahuan  cliffs  colony  desert  earth  exodus
factory  firewatch  forest  gradient  home  island  lake  lakeside  market  mojave  moon
mountains  room  sahara  street  tokyo  

Exemplos: 
test.sh -s beach       Define o papel de parede do estilo 'beach'
test.sh -p -s sahara   Define o papel de parede do estilo 'sahara' usando o pywal
```

+ Selecione o estilo que você gosta e execute -
```
$ dwall -s firewatch
[*] Usando o estilo: firewatch
```

### Configurar tarefa cron

Este programa foi criado especificamente para usar com um agendador de tarefas baseado em tempo, como o **cron** ou **systemd/Timers**. Então, após instalar este programa, você precisa configurar uma tarefa cron usando o `crontab` no seu sistema. Siga os passos abaixo para agendar uma tarefa para este programa - 
> Estou usando o `cronie` no Arch Linux aqui.

- Após instalar o `cron`, habilite e inicie o serviço cron -
```bash
# No Arch Linux
$ sudo systemctl enable cronie.service --now
```

- Certifique-se de que o serviço está habilitado e em execução -
```
$ systemctl status cronie.service
● cronie.service - Periodic Command Scheduler
     Loaded: loaded (/usr/lib/systemd/system/cronie.service; enabled; vendor preset: disabled)
     Active: active (running) since Sat 2020-12-26 14:39:31 IST; 5h 22min ago
   Main PID: 779 (crond)
```

- O Cron não é executado sob o servidor Xorg, portanto, ele não pode saber as variáveis de ambiente necessárias para iniciar uma aplicação do servidor Xorg, então elas terão que ser definidas. Descubra os valores das seguintes variáveis de ambiente - `SHELL, PATH, DISPLAY, DESKTOP_SESSION, DBUS_SESSION_BUS_ADDRESS, XDG_RUNTIME_DIR`
```
$ echo "$SHELL | $PATH | $DISPLAY | $DESKTOP_SESSION | $DBUS_SESSION_BUS_ADDRESS | $XDG_RUNTIME_DIR"

/usr/bin/zsh | /usr/local/bin:/usr/bin | :0 | Openbox | unix:path=/run/user/1000/bus | /run/user/1000
```

- Agora, crie uma tarefa cron horária para o **dwall** usando o `crontab` -
```bash
# exporte o editor para o crontab
$ export EDITOR=vim

# Edite seu crontab e adicione uma tarefa
$ crontab -e

# Adicione esta linha substituindo os valores da variável de ambiente e do estilo pelos seus
0 * * * * env PATH=/usr/local/bin:/usr/bin DISPLAY=:0 DESKTOP_SESSION=Openbox DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" /usr/bin/dwall -s firewatch

# verifique se a tarefa foi criada no seu crontab
$ crontab -l
0 * * * * env PATH=/usr/local/bin:/usr/bin DISPLAY=:0 DESKTOP_SESSION=Openbox DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" /usr/bin/dwall -s firewatch
```

- É isso, o **dwall** foi adicionado ao seu crontab e mudará o papel de parede a cada hora. Se você quiser mudar o estilo do papel de parede, basta remover a tarefa anterior e adicionar uma nova com outro estilo.
```bash
# delete a tarefa anterior
$ crontab -r

# Adicione uma nova tarefa com um estilo diferente
$ crontab -e
0 * * * * env PATH=/usr/local/bin:/usr/bin DISPLAY=:0 DESKTOP_SESSION=Openbox DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" /usr/bin/dwall -s bitday
```

### Como adicionar seus próprios papéis de parede

+ Baixe um conjunto de papéis de parede que você goste.
+ Renomeie os papéis de parede (devem ser **jpg/png**) para `0-23`. Se você não tiver imagens suficientes, crie links simbólicos para elas.
+ Crie um diretório em `/usr/share/dynamic-wallpaper/images` e copie seus papéis de parede para lá. 
+ Execute o programa, selecione o estilo e aplique-o.

**`Dicas`**
- Você pode usar o `dwall` para alternar entre seus papéis de parede favoritos a cada hora.
- Você pode usar o `dwall` como uma apresentação de slides de imagens, que pode definir suas fotos favoritas como papel de parede a cada hora ou a cada 15 minutos. Basta criar uma tarefa cron apropriada.

### Use Imagens HEIC

Você também pode querer usar papéis de parede do [Dynamic Wallpaper Club](https://dynamicwallpaper.club/). Para fazer isso, você precisa converter o arquivo de imagem `.heic` para o formato png ou jpg. Baixe um arquivo de papel de parede `.heic` que você goste e siga os passos abaixo para converter as imagens.

- Primeiro instale o `heif-convert` no seu sistema - 
```bash
# No Archlinux
$ sudo pacman -Sy libheif

# No Ubuntu ou Debian
$ sudo apt-get install libheif-examples

```

- Mova seu arquivo `.heic` para um diretório e execute o seguinte comando para converter as imagens - 
```bash
# mude para o diretório
$ cd Downloads/heic_images

# converta para imagens jpg
$ for file in *.heic; do heif-convert $file ${file/%.heic/.jpg}; done
```

- Agora que você tem as imagens, basta seguir os passos [acima](https://github.com/adi1090x/dynamic-wallpaper#How-to-add-own-wallpapers) para usar esses papéis de parede com o `dwall`.

**Mais Papéis de Parede:** Eu também criei mais alguns conjuntos de papéis de parede, que não foram adicionados a este repositório por causa de seu tamanho grande. Você pode baixar esses conjuntos de papéis de parede aqui - 
<p align="center">
  <a href="https://github.com/adi1090x/files/tree/master/dynamic-wallpaper/wallpapers"><img alt="undefined" src="https://img.shields.io/badge/Baixar-Aqui-blue?style=for-the-badge&logo=github"></a>
</p>

**`Conjuntos Disponíveis`**: `Catalina`, `London`, `Maldives`, `Mojave HD`, `Mount Fuji`, `Seoul`, e mais...

### Pré-visualizações

|Aurora|Beach|Bitday|Chihuahuan|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/aurora.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/beach.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/bitday.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/chihuahuan.gif)|

|Cliffs|Colony|Desert|Earth|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/cliffs.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/colony.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/desert.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/earth.gif)|

|Exodus|Factory|Forest|Gradient|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/exodus.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/factory.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/forest.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/gradient.gif)|

|Home|Island|Lake|Lakeside|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/home.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/island.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/lake.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/lakeside.gif)|

|Market|Mojave|Moon|Mountains|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/market.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/mojave.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/moon.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/mountains.gif)|

|Room|Sahara|Street|Tokyo|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/room.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/sahara.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/street.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/tokyo.gif)|

### Problemas Comuns

**1. O papel de parede não está mudando**: Se o seu papel de parede não estiver mudando, abra um problema e me mostre a saída de `echo $DESKTOP_SESSION`.

**2. Não funciona no XFCE**: Se este script não estiver funcionando no xfce, abra o terminal e execute `xfconf-query -c xfce4-desktop -m` e mude o papel de parede (qualquer um) através do *xfce4-settings-manager*. <br />
No terminal, o *xfconf-query* imprimirá linhas começando com `set:`, que mostram quais propriedades foram alteradas, verifique os valores de `screen` e `monitor` e modifique o script de acordo.
```bash
109   ## Para XFCE
110   if [[ "$OSTYPE" == "linux"* ]]; then
111      SCREEN="0"
112      MONITOR="1"
113   fi

```

3. **Autostart**: Se você quiser iniciar o script automaticamente com o desktop, você pode adicioná-lo ao arquivo de autostart do seu WM e se não funcionar para você, você pode criar um `arquivo de desktop` no diretório `$HOME/.config/autostart`.
```bash
$ cd $HOME/.config/autostart && touch dwall.desktop

# Adicione isto ao arquivo dwall.desktop

[Desktop Entry]
Name=Dynamic Wallpaper
Comment=Set desktop background according to current time.
Exec=/usr/bin/dwall -s firewatch &
Type=Application
Icon=wallpaper
Categories=Accessories;
```
> Alternativamente, você também pode colocar o comando `/usr/bin/dwall -s firewatch &` no seu arquivo `~/.bashrc`.

### Informações Rápidas

+ No KDE, o `dwall` muda o papel de parede em todas as Atividades.
+ Ao usar com o `pywal`, a cor de outras aplicações (Terminal, polybar, rofi, etc) mudará da maneira que você configurou essas aplicações. Isso é com você.
+ Você pode adicionar **`dwall -s estilo &`** ao arquivo de autostart do seu WM para definir/restaurar o papel de parede após o login/reinicialização.
+ Você também pode criar um crontab `@reboot` para definir o papel de parede apropriado na inicialização.