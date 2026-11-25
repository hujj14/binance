#!/bin/bash
# Получаем токен через curl и сохраняем в переменную
TOKEN=$(curl -s -X POST http://localhost:8080/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=hacker&password=supersecret" | grep -oP '(?<="access_token":")[^"]*')

# Подставляем токен в конфиг ZAP
sed -i "s|replacer.full_list(0).replacement=Bearer |replacer.full_list(0).replacement=Bearer $TOKEN|" zap-auth.prop