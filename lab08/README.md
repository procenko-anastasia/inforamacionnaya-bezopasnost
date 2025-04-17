# Лабораторная работа №8
## Обнаружение утечек секретов с использованием Gitleaks

### Цель работы  
Изучить основы работы с инструментом **Gitleaks** для обнаружения секретов (API-ключей, паролей, токенов и др.) в репозиториях Git. Получить практические навыки настройки и использования Gitleaks для анализа кода и предотвращения утечек конфиденциальной информации.

---

## Теоретическая часть

**Gitleaks** — инструмент с открытым исходным кодом, предназначенный для поиска утечек чувствительных данных в Git-репозиториях. Он используется как разработчиками, так и специалистами по информационной безопасности для обеспечения безопасности кода на всех этапах разработки.

---

## Практическая часть

### Задание 1: Установка Gitleaks

- **Для macOS/Linux:**
```bash
  brew install gitleaks
```
Проверка установки:
`gitleaks --version`

### Задание 2: Сканирование Git-репозитория

Cоздала новый тестовый репозиторий:
```
mkdir test-repo
cd test-repo
git init
```
Добавила тестовые файлы с «секретами»:
`config.py`
```
API_KEY = "12345-abcdef-67890-ghijk"
DATABASE_PASSWORD = "s3cr3tP@ssw0rd"
```
`.env`
```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```
Сделала коммит:
```
git add .
git commit -m "Add config files"
```
Запустила Gitleaks:
`gitleaks detect --source . -v`
Результат команды:
```
    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

Finding:     API_KEY = "12345-abcdef-67890-ghijk"
Secret:      12345-abcdef-67890-ghijk
RuleID:      generic-api-key
Entropy:     4.386842
File:        config.py
Line:        1
Commit:      6d607631465d3bb4c756510153bb436006463f73
Author:      procenko-anastasia
Email:       procenko.anastasia123@mail.ru
Date:        2025-04-17T15:34:14Z
Fingerprint: 6d607631465d3bb4c756510153bb436006463f73:config.py:generic-api-key:1

6:34PM INF 1 commits scanned.
6:34PM INF scanned ~176 bytes (176 bytes) in 55.1ms
6:34PM WRN leaks found: 1
```

### Задание 3: Настройка конфигурации Gitleaks
Cоздала файл `gitleaks-config.toml` со следующими правилами:
```
title = "Gitleaks Config"

[[rules]]
id = "api-key"
description = "API Key"
regex = '''[a-zA-Z0-9]{32}'''
tags = ["key", "api"]

[[rules]]
id = "password"
description = "Password"
regex = '''(?i)password\s*=\s*["']([^"']+)["']'''
tags = ["password", "secret"]
```
Запустила сканирование с конфигурацией:
```
gitleaks detect --source . --config gitleaks-config.toml -v
```
Убедилась, что используются кастомные правила и вывод соответствует ожидаемому результату.
Вывод:
```

    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

Finding:     DATABASE_PASSWORD = "s3cr3tP@ssw0rd"
Secret:      s3cr3tP@ssw0rd
RuleID:      password
Entropy:     3.182006
Tags:        [password secret]
File:        config.py
Line:        2
Commit:      6d607631465d3bb4c756510153bb436006463f73
Author:      procenko-anastasia
Email:       procenko.anastasia123@mail.ru
Date:        2025-04-17T15:34:14Z
Fingerprint: 6d607631465d3bb4c756510153bb436006463f73:config.py:password:2

6:35PM INF 1 commits scanned.
6:35PM INF scanned ~176 bytes (176 bytes) in 46ms
6:35PM WRN leaks found: 1
```
