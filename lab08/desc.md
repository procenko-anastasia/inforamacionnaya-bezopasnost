Лабораторная работа №X. Работа с Nightfall Python SDK для обнаружения и маскировки чувствительных данных

Цель работы: Изучить основы использования Nightfall Python SDK для обнаружения, классификации и защиты конфиденциальной информации в соответствии с ГОСТ 19.

Оборудование:
- Компьютер с установленной операционной системой
- Python 3.8+
- Nightfall Python SDK
- Текстовый редактор или IDE

Ход работы:

1. Установка Nightfall SDK

```bash
pip install nightfall
```

2. Инициализация клиента

```python
from nightfall import Nightfall, DetectionRule, Detector

# Создание клиента с API ключом
API_KEY = "your_api_key_here"
nightfall_client = Nightfall(API_KEY)

# Настройка правила детекции
detection_rule = DetectionRule(
    name="Sensitive Data Rule",
    detectors=[
        Detector(detector_type="CREDIT_CARD"),
        Detector(detector_type="EMAIL_ADDRESS")
    ]
)
```
Описание: Создаем клиент Nightfall и задаем правило для обнаружения кредитных карт и email адресов.

3. Обнаружение чувствительных данных

```python
text_to_scan = "My credit card number is 4111111111111111 and my email is test@example.com"

scan_result = nightfall_client.scan_text(
    text=text_to_scan,
    detection_rules=[detection_rule]
)

print(scan_result)
```
Ожидаемый результат:
```
[
    {'match': '4111111111111111', 'type': 'CREDIT_CARD'},
    {'match': 'test@example.com', 'type': 'EMAIL_ADDRESS'}
]
```

4. Маскировка данных

```python
masked_text = nightfall_client.redact_text(
    text=text_to_scan,
    detection_rules=[detection_rule]
)

print(masked_text)
```
Ожидаемый результат:
```
"My credit card number is [CREDIT_CARD] and my email is [EMAIL_ADDRESS]"
```

5. Работа с файлами

```python
with open('example.pdf', 'rb') as file:
    file_data = file.read()

file_scan_result = nightfall_client.scan_file(
    file_data=file_data,
    detection_rules=[detection_rule]
)

print(file_scan_result)
```

6. Дополнительные настройки детекторов

```python
custom_detection_rule = DetectionRule(
    name="Custom Sensitive Data Rule",
    detectors=[
        Detector(
            detector_type="REGEX",
            regex=r"\b\d{6}\b", # Пример: поиска шестизначных чисел
            name="Custom Regex"
        )
    ],
    min_score=0.7
)

custom_scan_result = nightfall_client.scan_text(
    text="Here is a number: 123456",
    detection_rules=[custom_detection_rule]
)

print(custom_scan_result)
```

7. Логирование и отчетность

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    scan_result = nightfall_client.scan_text(
        text=text_to_scan,
        detection_rules=[detection_rule]
    )
    logging.info("Scan successful: %s", scan_result)
except Exception as e:
    logging.error("Scan failed: %s", str(e))
```

Задания для самостоятельной работы:

1. Создайте правило для обнаружения паспортных данных РФ
2. Реализуйте маскировку различных типов данных
3. Проведите сканирование нескольких файлов разных форматов
4. Настройте собственные регулярные выражения для обнаружения специфичных данных вашей организации
5. Внедрите логирование всех операций сканирования

Контрольные вопросы:

1. Что такое Nightfall SDK?
2. Какие типы данных можно обнаруживать с помощью Nightfall?
3. Как настроить пользовательские детекторы?
4. Какие форматы файлов поддерживаются для сканирования?
5. Как организовать маскировку обнаруженных данных?
