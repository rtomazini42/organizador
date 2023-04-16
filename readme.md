# Organizador simples via bash para sistemas Unix

Esse é um simples organizador via bin/bash, você precisa usar o Sudo para autorizar ele a organizar seus arquivos.
A ideia é aplicar ele na sua pasta de download, classificando os arquivos em algumas pastas:

* Audio
* Executavel
* Textos
* imagens
* Video
* Torrent
* Scripts
* Outros

Para usar basta rodar o organizador.sh na pasta que você quer organizar com o comando abaixo:

```
sudo bash organizador.sh
```

Inserir sua senha e ele começa organizar seus arquivos.

Ao final haverá a opção de manter ou deletar arquivos e pastas vazias, qualquer número abaixo de 1 irá deletar as pastas e arquivos vazios (os que contém 0kb)

O organizador sera guardado na pasta Organizador ao final do processo, para que você possa ultilizar ele novamente quando precisar.

#### Testado em Pop!OS 22.04



# Versão Windows
A versão Windows foi feita e testada em Windows 10 em 2023 com Python 3.9, funcionou aparentemente bem, mas não garanto seu funcionamento em todos os casos.
Para rodar o script "organizadorWindows.py" siga os seguintes passos:

* Abra o terminal do Windows. Para isso, clique no botão "Iniciar" e digite "cmd" na barra de pesquisa.

* Navegue até o diretório onde o arquivo "organizadorWindows.py" está localizado. Para isso, utilize o comando "cd" seguido do caminho completo do diretório. Exemplo: cd C:\Users\seu_usuario\Downloads

* Digite "python organizadorWindows.py" e pressione enter para executar o script.

* O script irá perguntar se você quer organizar os arquivos na pasta atual. Digite "1" para sim ou "2" para não.

* Se você escolher "1", o script irá criar as pastas necessárias e mover os arquivos para suas respectivas pastas.

* O script irá perguntar se você quer deletar as pastas e arquivos vazios. Digite "1" para sim ou "2" para não.

* Se você escolher "1", o script irá deletar as pastas e arquivos vazios.

* Quando o script terminar de executar, ele irá exibir a mensagem "Feito" e "Obrigado por usar!".


#### Testado em Windows 10 2023