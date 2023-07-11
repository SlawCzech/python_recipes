# Algorytm tworzenia funkcjonalności django

1. Zaprojektowanie funkcjonalności
    - określenie wymagań
    - dopasowanie rozwiązań do istniejącej architektury 
    - ocena wpływu na wydajność aplikacji
    - porównanie różnych typów rozwiązań (przegląd i wybór technologii) - ma spełniać dzisiejsze i przyszłe wymagania (dług technologiczny i elastyczność)
    - draft ERD 
    - draft do API Diagram 
    - draft do flow
2. Czy potrzebujemy django app?
    - `python manage.py startapp <app_name>`
    - dodaj do installed apps -> settings.py
3. Analiza czy potrzebujemy dane?
   - narysuj/aktualizuj ERD diagram na kartce
   - implementacja w models.py
   - czy potrzebny jest custom manager?
   - czy warto użyć fat-models-skinny-view-pattern? czyli logika w modelach?
   - `python manage.py makemigrations <app_name>`
   - `python manage.py migrate <app_name>`
   - troubleshooting: 
     - upewnij się, że apka jest w installed apps, 
     - że `__init__.py` jest w migrations/
     - że nazwa migracji nie została już zaaplikowana
   - unit tests -> pytest
4. Czy potrzebujemy zarządzać tym zasobem z CMS(django admin)?
   - rejestrujemy modele w admin.py, customowa konfiguracja
   - prosto `admin.site.register`
   - profesjonalnie:
     - utworzenie klasy konfiguracji admina
     - konfiguruje się 2 widoki: listy i edycji
     - lista: wyszukiwarka, filtry, edycja inline, sortowanie, kolumny z danymi, akcje (najważniejsze)
     - edycja: rodzaj formularza oraz połączenie wielu formularzy (można dograć customowy JS i formularze)
     - upewnij się, że `__str__` działają poprawnie
     - testy funkcjonalne (pod kątem tego, jak użytkownik by używał funkcjonalności) -> pytest i selenium lub JavaScript i Cypress
5. Czy wystawiamy dane w widoku?
   - tworzymy plik serializers.py (format danych)
   - unit tests
6. Tworzymy widoki (logike) -> jeżeli pełny CRUD to ViewSets
   - Dobieramy odpowiednią klase do obsługi widoku [wyszukiwarka widoków](https://www.cdrf.co)
   - Widok musi zwracać response lub redirect
   - Logika uprawnień permission.py
   - Unit tests
7. Tworzymy lokalny router
   - W pliku urls.py tworzymy urlpatterns lub router
   - Podpinamy lokalne urls do globalnych urls -> config/urls.py
   - Unit tests
8. Sprawdzenie dokumentacji OpenAPI(swagger)
9. Postman i stworzenie kolekcji
   - Wyeksportowanie kolekcji do repozytorium