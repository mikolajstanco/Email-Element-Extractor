# Email Element Extractor

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Playwright / E2E](https://img.shields.io/badge/tests-E2E_Helper-brightgreen.svg)]()

## 📌 O projekcie
**Email Element Extractor** to lekkie narzędzie pomocnicze przeznaczone do wspomagania testów End-to-End (E2E) i automatyzacji procesów QA. 

Jego głównym zadaniem jest integracja z API Gmaila, wyszukiwanie wiadomości o określonym temacie i dynamiczne ekstrahowanie z ich wnętrza specyficznych elementów HTML (np. kodów 2FA, linków aktywacyjnych czy kodów rabatowych).

### 🎯 Główne funkcje:
* **Integracja z Gmail API:** Bezpieczne i oficjalne logowanie via OAuth2.
* **Generyczna ekstrakcja (CSS Selector):** Zamiast szukać elementów na "sztywno", narzędzie pozwala na zdefiniowanie dowolnych tagów i stylów CSS szukanego elementu w pliku konfiguracyjnym.
* **Inteligentne parsowanie adresów e-mail (Regex):** Skrypt radzi sobie z niestandardowymi nagłówkami nadawców (np. *Hide My Email* od Apple iCloud), precyzyjnie wyciągając czysty adres e-mail za pomocą wyrażeń regularnych.
* **Automatyczne oznaczanie jako przeczytane:** Zapobiega wielokrotnemu przetwarzaniu tych samych wiadomości.

## ⚙️ Architektura
Projekt został podzielony zgodnie z zasadą Single Responsibility:
* `Main.py` - główna pętla i logika przetwarzania.
* `GoogleAuth.py` - moduł autoryzacyjny OAuth2.
* `GoogleManagement.py` - wrapper na metody Gmail API (abstrakcja).
* `settings.json` - plik konfiguracyjny oddzielający dane testowe od logiki.

## 🚀 Jak zacząć?

### 1. Wymagania
* Python 3.8+
* Projekt w Google Cloud Console (włączone Gmail API).
* Pobrany plik `credentials.json` (klucz klienta OAuth 2.0).

### 2. Instalacja
Sklonuj repozytorium i zainstaluj niezbędne biblioteki:

```bash
git clone [https://github.com/mikolajstanco/Email-Element-Extractor.git](https://github.com/mikolajstanco/Email-Element-Extractorgit)
cd Email-Element-Extractor
pip install -r requirements.txt
