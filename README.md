# Procurement Studio & CRM — dokumenty, oferty i kampanie

Case study of a procurement analysis workspace linked to a sales CRM for the landscaping industry.

**Zakres publiczny:** Studium przypadku wdrożenia.

## Problem

Rozwiązanie wspiera firmę z branży zieleni w analizie dokumentacji przetargowej, przygotowywaniu wycen i prowadzeniu kontaktów z wykonawcami. Składa się z lokalnego środowiska analitycznego Studio oraz oddzielnego panelu CRM.

## Jak działa projekt

1. Studio zbiera ogłoszenia BZP i TED oraz załączniki. Pliki są deduplikowane po SHA-256, a ekstrakcja obsługuje dokumenty biurowe, PDF i skany.
2. OCR, reguły oraz model lokalny zamieniają zakres dokumentacji na rekordy z odwołaniem do pliku, strony i fragmentu źródłowego. Elementy o niskiej pewności trafiają do operatora.
3. CRM odbiera przygotowane rekordy przez warstwę synchronizacji. Wspiera kolejkę wiadomości, wykluczenia, odpowiedzi, kalendarz oraz sporządzanie ofert PDF z pozycji katalogowych.
4. Uprawnienia, audyt i dziennik zdarzeń pomagają oddzielić przygotowanie danych od obsługi kampanii. Rekord ma status wysłanego po odpowiedzi SMTP.

## Technologie

React, TypeScript, FastAPI, Pydantic, SQLAlchemy, SQLite WAL, APScheduler, Ollama, Windows OCR, SMTP/IMAP.

## Co można sprawdzić

Repozytorium prezentuje architekturę wdrożenia. Publiczne demo procesu CRM z fikcyjnymi danymi znajduje się w [All Day OS](https://github.com/AlexDzien/all-day-os).
