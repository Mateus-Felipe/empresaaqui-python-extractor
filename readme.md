# How it works

Run this command to open chrome in debug mode (windows): "C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/chrome-debug"
change the location if you need

## Download chrome driver
download chrome driver in the official website (choose the right version)
the version need be the same of your chrome
https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
put the path to your code in main.py

## the chrome

in the already openned chrome window, start a search with filter
the tested url is something like this: 
https://www.empresaqui.com.br/acesso/Empresas.php?ModalAcao=&ModalCNAE=&ModalAcao=

# make the search

the result will be added to dados_extraidos.xlsx file
the old data will be added automatically

if you got an error, just run again :) (yeah, i need solve this bug, but i did it in less than 15 minutes)
