# Log de Configuração do Papel de Parede Dinâmico

Este arquivo documenta os passos executados para configurar o script de papel de parede dinâmico para funcionar corretamente através do `cron`.

## Problema

O papel de parede dinâmico não estava sendo atualizado automaticamente porque o `cron job` necessário não estava configurado. Tentativas de adicionar o `cron job` diretamente falharam devido a erros de sintaxe na linha do `crontab`.

## Solução

Para resolver o problema de forma robusta, um script wrapper foi criado para ser chamado pelo `cron`.

1.  **Criação do Script Wrapper:**
    Um script chamado `dwall_cron.sh` foi criado no diretório do projeto. Este script define as variáveis de ambiente necessárias e depois executa o comando `dwall`.

    **Conteúdo do `dwall_cron.sh`:**
    ```bash
    #!/bin/bash
    export PATH="/home/thiago_dev/.nvm/versions/node/v20.19.5/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/thiago/.local/bin"
    export DISPLAY=":1"
    export DESKTOP_SESSION="pop"
    export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
    /usr/bin/dwall -s bitday
    ```

2.  **Permissão de Execução:**
    O script foi tornado executável com o comando:
    ```bash
    chmod +x /home/thiago_dev/dynamic-wallpaper/dwall_cron.sh
    ```

3.  **Configuração do Cron Job:**
    O `crontab` do usuário foi configurado para executar o script `dwall_cron.sh` a cada hora. A seguinte linha foi adicionada ao `crontab`:
    ```
    0 * * * * /home/thiago_dev/dynamic-wallpaper/dwall_cron.sh
    ```

## Como Mudar o Tema

Para alterar o tema do papel de parede, edite o arquivo `dwall_cron.sh` e mude o valor do parâmetro `-s`. Por exemplo, para usar o tema `aurora`, altere a última linha para:
```bash
/usr/bin/dwall -s aurora
```
