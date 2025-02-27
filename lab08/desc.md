Лабораторная работа №X. ### **Лабораторная работа №16: Обнаружение утечек секретов с использованием Gitleaks**

**Цель работы:**  
Изучить основы работы с инструментом Gitleaks для обнаружения секретов, таких как пароли, API-ключи и токены, в репозиториях Git и файлах. Научиться настраивать и использовать Gitleaks для анализа кода и предотвращения утечек конфиденциальной информации.

**Теоретическая часть:**  
Gitleaks — это инструмент с открытым исходным кодом, предназначенный для поиска секретов (например, API-ключей, токенов, паролей) в репозиториях Git, файлах и других источниках. Он помогает разработчикам и командам безопасности выявлять утечки конфиденциальных данных на ранних этапах.

**Практическая часть:**

#### Задание 1: Установка Gitleaks
1. Установите Gitleaks на вашу систему:
   - Для Linux/macOS:
     ```bash
     brew install gitleaks
     ```
   - Для Windows (с использованием Scoop):
     ```bash
     scoop install gitleaks
     ```
   - Альтернативный способ (установка из исходного кода):
     ```bash
     git clone https://github.com/gitleaks/gitleaks.git
     cd gitleaks
     make build
     ```

2. Проверьте установку, выполнив команду:
   ```bash
   gitleaks --version
   ```

#### Задание 2: Сканирование Git-репозитория
1. Создайте тестовый Git-репозиторий:
   ```bash
   mkdir test-repo
   cd test-repo
   git init
   ```

2. Добавьте тестовые файлы с секретами:
   - Создайте файл `config.py` с содержимым:
     ```python
     API_KEY = "12345-abcdef-67890-ghijk"
     DATABASE_PASSWORD = "s3cr3tP@ssw0rd"
     ```
   - Создайте файл `.env` с содержимым:
     ```
     AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
     AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
     ```

3. Добавьте файлы в репозиторий и сделайте коммит:
   ```bash
   git add .
   git commit -m "Add config files"
   ```

4. Запустите сканирование репозитория с помощью Gitleaks:
   ```bash
   gitleaks detect --source . -v
   ```

5. Проанализируйте результаты сканирования. Gitleaks выведет список найденных секретов с указанием файла и строки.

#### Задание 3: Настройка конфигурации Gitleaks
1. Создайте конфигурационный файл `gitleaks-config.toml` для настройки правил обнаружения:
   ```toml
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

2. Запустите сканирование с использованием конфигурационного файла:
   ```bash
   gitleaks detect --source . --config gitleaks-config.toml -v
   ```

3. Убедитесь, что Gitleaks использует ваши правила для обнаружения секретов.

#### Задание 4: Интеграция Gitleaks в CI/CD
1. Настройте Gitleaks для автоматического сканирования в CI/CD (например, GitHub Actions):
   - Создайте файл `.github/workflows/gitleaks.yml`:
     ```yaml
     name: Gitleaks Scan

     on: [push, pull_request]

     jobs:
       gitleaks:
         runs-on: ubuntu-latest
         steps:
           - name: Checkout code
             uses: actions/checkout@v2

           - name: Run Gitleaks
             uses: gitleaks/gitleaks-action@v2
             with:
               config-path: ./gitleaks-config.toml
     ```

Эта лабораторная работа позволяет студентам получить практический опыт работы с инструментами для обнаружения секретов и предотвращения утечек конфиденциальной информации в разработке программного обеспечения.

Задания для самостоятельной работы:

1. Создайте правило для обнаружения паспортных данных РФ
2. Реализуйте маскировку различных типов данных
3. Проведите сканирование нескольких файлов разных форматов
4. Настройте собственные регулярные выражения для обнаружения специфичных данных вашей организации
5. Внедрите логирование всех операций сканирования
