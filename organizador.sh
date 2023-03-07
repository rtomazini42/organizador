#! /bin/bash

echo "Bem vindo! É na pasta que você está rodando o script que você quer organizar?"
echo "Responda 1 para sim"
read resposta
if [ $resposta -ge 2 ]
 then
	echo "bye"
	exit 0 

fi
echo "Rodando"

echo "Criando pastas"
mkdir Audio
mkdir Executavel
mkdir Textos
mkdir Imagens
mkdir Video
mkdir Torrent
mkdir Scripts
mkdir Zips
mkdir Outros

mkdir Organizador
mv organizador.sh Organizador/
mv readme.md Organizador/

mv  *.mp3 *.ogg *.flac *.acc *.wma *.alac *.aiff *.pcm *.wav Audio/ 
mv  *.deb *.app *.iso *.exe  Executavel/
mv  *.epub *.txt *.pdf  Textos/
mv  *.jpg *.png *.bmp *.jpeg *.svg .gif Imagens/
mv  *.mp4 *.flv *.mpeg *.webm *.mkv *.vob *.ogv *.avi *.MTS *.mov *.rm *.rmvb *.viv *.amv *.mpg *.m4p *.m4v *.mpe *.m2v *.svi *.3gp *.3g2 Video/
mv  *.torrent *.magnet Torrent/
mv  *.py *.sh *.cpp *.js *.rs *rslib Scripts/
mv  *.zip *.rar Zips/
mv  *.* Outros/

echo "Deletar pastas e arquivos vazios?"
echo "Responda 1 para sim"
read deletar
if [ $deletar -ge 2 ]
 then
        echo "Obrigado por usar!"
        exit 0 

fi
find -empty -delete

echo "Feito"
echo "Obrigado por usar!"

