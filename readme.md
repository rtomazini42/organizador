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

