#!/bin/bash
clear

echo -e "\033[0;32m \n**** listes des fonctions(snake_case: show_nom_table add_nom_table valid_add_nom_table delete_nom_table edit_nom_table valid_edit_nom_table) :"
grep "def "  app.py | uniq -c

echo -e "\033[0;32m \n**** listes des fichiers (snake_case: add_table.html edit_table.html show_table.html)  : "
ls templates/*

echo -e "\033[0;31m \n***** listes des routes (spinal case : /nom-table/show /nom-table/edit /nom-table/add ) \033[0m"
grep "@app.route"  app.py

echo -e "\033[0;32m \n**** listes des paramètres POST (CamelCase : clés des dictionnaires, sauf la clé étrangére) :"
grep "request.form.get"  app.py | uniq -c

echo -e " \033[0m"

code  app.py &

killall python3
flask --debug  --app app  run   --host 0.0.0.0