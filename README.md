<!-- Papel de Parede Dinâmico -->

<p align="center">
  <img src="https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/logo.png">
</p>

<p align="center">Um script <code>python</code> simples para definir papéis de parede de acordo com a hora atual, usando o <b>agendador de tarefas cron</b>. <br> Fork adaptado para funcionar nativamente no <b>Pop!_OS</b>.</p>

![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/main.gif) <br />

### Visão Geral

+ 25+ tipos diferentes de conjuntos de papéis de parede (HD/UHD/4K/5K).
+ Usuários podem adicionar seus próprios papéis de parede.
+ Com o `Cron`, o papel de parede muda de acordo com a hora, ao longo do dia.
+ Focado e testado para o ambiente de desktop do **Pop!_OS**.

### Dependências

Este script requer apenas o `python3`. O `gsettings`, necessário para alterar o papel de parede, já vem instalado no Pop!_OS.

### Instalação

Basta clonar este repositório para sua máquina local.

```bash
git clone https://github.com/ThiagoResende88/dynamic-wallpaper.git
cd dynamic-wallpaper
```

### Uso

O script agora é autônomo e utiliza a pasta `images` dentro do próprio projeto.

#### Definindo o Tema

Para definir um tema de papel de parede, execute o script `dynamic_wallpaper.py` com o argumento `--theme`, seguido pelo nome da pasta do tema. É importante incluir as variáveis de ambiente no início do comando.

Por exemplo, para o tema `aurora`:

```bash
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus DISPLAY=:1 python3 dynamic_wallpaper.py --theme aurora
```

Isso salvará sua escolha e definirá o papel de parede para a hora atual.

#### Alterando o Papel de Parede Manualmente

Para acionar manualmente uma troca de papel de parede para a hora atual (usando o tema salvo), simplesmente execute o script sem nenhum argumento (mas com as variáveis de ambiente):

```bash
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus DISPLAY=:1 python3 dynamic_wallpaper.py
```

### Automação com Cron

Para fazer a troca de papel de parede automaticamente a cada hora, você precisa adicionar uma tarefa cron.

1.  Abra seu crontab para edição:

    ```bash
    crontab -e
    ```

2.  Adicione a seguinte linha ao arquivo, **substituindo `/path/to/` pelo caminho completo** onde você clonou o repositório:

    ```
    0 * * * * DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus DISPLAY=:1 python3 /path/to/dynamic-wallpaper/dynamic_wallpaper.py
    ```

3.  Salve e saia do editor. Seu papel de parede agora mudará automaticamente a cada hora.

### Automação na Inicialização (Autostart)

O `cron` funciona muito bem, mas tem uma limitação: ele não executa tarefas que foram perdidas enquanto o computador estava desligado. Isso significa que se você ligar o computador, o papel de parede não será atualizado para o horário correto até a próxima hora cheia.

Para resolver isso, podemos configurar o script para ser executado toda vez que o sistema é iniciado.

#### Configuração

Para facilitar, um script de configuração foi adicionado ao projeto. Para usá-lo, basta executar os seguintes comandos no seu terminal, a partir da pasta do projeto:

```bash
chmod +x setup_autostart.sh
./setup_autostart.sh
```

Isso criará um arquivo de configuração em `~/.config/autostart/` que fará com que o `dynamic_wallpaper.py` seja executado automaticamente toda vez que você fizer login.

#### Como Funciona em Conjunto com o Cron

Usar o autostart e o cron juntos oferece a melhor experiência:

-   **Autostart**: Garante que o papel de parede correto seja definido assim que você liga o computador e faz login.
-   **Cron**: Continua atualizando o papel de parede a cada hora, garantindo que ele permaneça em sincronia com o tempo ao longo do dia.

Portanto, é recomendado usar **ambas** as formas de automação.

### Como configurar um atalho (alias)

Para evitar ter que digitar o comando completo toda vez, você pode criar um atalho chamado `dwall`.

1.  Abra o arquivo de configuração do seu shell (normalmente `~/.bashrc`):
    ```bash
    gedit ~/.bashrc
    ```

2.  Adicione a seguinte linha no final do arquivo, **substituindo `/path/to/` pelo caminho completo** onde você clonou o repositório:
    ```bash
    alias dwall="DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus DISPLAY=:1 python3 /path/to/dynamic-wallpaper/dynamic_wallpaper.py"
    ```

3.  Salve o arquivo e reinicie seu terminal ou execute `source ~/.bashrc`.

4.  Agora você pode usar o atalho `dwall`. Por exemplo:
    ```bash
    dwall --theme moon
    ```

### Como adicionar seus próprios papéis de parede

+ Baixe um conjunto de papéis de parede que você goste.
+ Renomeie os papéis de parede (devem ser **jpg/png**) para `0-23`. Se você não tiver imagens suficientes, crie links simbólicos para elas.
+ Crie um diretório dentro da pasta `images` deste projeto e copie seus papéis de parede para lá.
+ Execute o script com `--theme` para usar seu novo tema.

### Use Imagens HEIC

Você também pode querer usar papéis de parede do [Dynamic Wallpaper Club](https://dynamicwallpaper.club/). Para fazer isso, você precisa converter o arquivo de imagem `.heic` para o formato png ou jpg. Baixe um arquivo de papel de parede `.heic` que você goste e siga os passos abaixo para converter as imagens.

- Primeiro instale o `heif-convert` no seu sistema -
```bash
# No Ubuntu ou Debian (como o Pop!_OS)
$ sudo apt-get install libheif-examples
```

- Mova seu arquivo `.heic` para um diretório e execute o seguinte comando para converter as imagens -
```bash
# mude para o diretório
$ cd /path/to/heic_images

# converta para imagens jpg
$ for file in *.heic; do heif-convert $file ${file/%.heic/.jpg}; done
```

- Agora que você tem as imagens, basta seguir os passos da seção "Como adicionar seus próprios papéis de parede".

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
