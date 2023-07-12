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
     - conftest + fixtures
     - markery
     - dobrze korzystać ze schematów dla funkcjonalności
4. Czy potrzebujemy zarządzać tym zasobem z CMS (django admin)?
   - rejestrujemy modele w admin.py, customowa konfiguracja
   - prosto `admin.site.register`
   - profesjonalnie:
     - utworzenie klasy konfiguracji admina
     - konfiguruje się 2 widoki: listy i edycji
     - lista: wyszukiwarka, filtry, edycja inline, sortowanie, kolumny z danymi, akcje (najważniejsze)
     - edycja: rodzaj formularza oraz połączenie wielu formularzy (można dograć customowy JS i formularze)
     - upewnij się, że `__str__` działają poprawnie
     - testy funkcjonalne (pod kątem tego, jak użytkownik by używał funkcjonalności) -> pytest i selenium lub JavaScript i Cypress
5. Czy użytkownik powinien wprowadzić dane?
    - jeśli monolit, to Django Forms -> forms.py
      - `forms.Form` - formularz bez automatycznego zapisu danych do bazy, np. contact form
      - `forms.ModelForm` - automatyczny zapis do bazy
      - `formsets` - najlepiej użyć factory function
        - `BaseFormSet` - nie jest oparty na modelu, zwielokrotnienie tego samego formularza
        - `BaseModelFormSet` - tworzenie formularza wielokrotnego na bazie jednego modelu
        - `BaseInlineFormSet` - pozwala robić formularz na modelu połączonym z innym modelem przez Foreign Key
    - Custom Validators? -> validators.py
      - tworzymy przez metodę w formularzu clean_<field_name>() za pomocą funkcji bądź klasy
    - Customowe pola w formularzu?
      - pamiętaj o widgetach
      - jeśli widgety nie pomogą, to można tworzyć własne pola na klasie bazowej Field
    - Czy potrzebujemy ładnego wyglądu? 
      - crispy forms + template package
    - jeśli Django REST API
      - tworzymy serializatory -> serializers.py
        - `serializers.Serializer` - analogicznie do formularzy
        - `serializers.ModelSerializer` - analogicznie do formularzy
    - unittests 
6. Czy funkcjonalność potrzebuje logiki? 
   - funkcje czy klasy -> preferujemy klasy generyczne (mała ilość kodu, mniejsza redundancja, zoptymalizowane działanie)
   - czy potrzebujemy CRUDa?
     - dla REST API -> ViewSets
   - czy potrzebujemy zdefiniować permissions? 
     - ograniczenia dla użytkowników w zależności od tego jaki mają status
     - najlepiej korzystać z wbudowanych permissions
   - widok może zwracać tylko Response albo Redirect
   - czy widok potrzebuje robić zapytania w tle do API 
     - zdefiniowanie funkcji lub metod asynchronicznych (async) - upewnić się, że apka działa przez asgi (nie wsgi)
   - unittests
7. Czy potrzebuje warstwę prezentacji HTML?
    - sprawdzić konfigurację Django Templates w `settings.py` -> `APP_DIR=True`
    - folder `app_name/templates/app_name/template_name.html` 
    - sprawdzić czy widok przekazuje kontekst (dane do templatki)
    - czy potrzebujemy globalny kontekst? 
      - settings.py -> TEMPLATES -> OPTIONS -> context_processors -> dodaj swoją funkcję 
    - Django Templates wskazówki:
      - odpowiednia hierarchia templatek (bloki i extend, raczej negatywny wpływ na szybkość renderowania)
      - pamiętać o partials (fragmenty HTML wstawiane przez include)
      - pamiętać o makrach (mini skrypty, np. do formularzy)
      - pamiętać o filtrach do wyświetlanych danych np. formatowanie daty (można je tworzyć samemu)
      - w templatkach unikamy logiki (jeśli się da)
      - testujemy funkcjonalnie i end2end (core'owa logika apki) -> pytest + selenium lub cypress
8. Lokalny routing 
   - `app_name/urls.py` -> urlpatterns
   - pamiętamy o zdefiniowaniu `app_name` czyli namespace dla path (gdy jest dużo endpointów) 
   - zdefiniować path do każdego endpointa
   - funkcja path() przyjmuje tylko widoki funkcyjne, stąd w widokach klasy custom constructor as_view()
   - dla ViewSetów definiujemy router, bo automatyzuje opcję użycia kilku metod HTTP na jednym endpoincie (GET, POST itp.)
   - sprawdzić czy endpointy się nie dublują 
   - endpointy przyjmują zmienne - warto używać slug (przyjazne nazwy endpointa)
   - unittests + api tests
   - dla REST API warto stworzyć kolekcję Postmana
9. Główny router
   - podpięcie do global url `config/urls.py`
10. Podpięcie funkcjonalności do jakiegoś linka/menu 
11. Sprawdzić ręcznie czy działa
12. Profit
13. Bonus:
    - LiveTemplates dla każdego problemu
    - GitHub Gist dla wszystkich problemów
    - portfolio aplikacji na dysku (żeby kopiować gotowy kod)
    - przygotowane aplikacje django, których najczęściej się używa
    - skróty klawiszowe na blachę


PRZEPISAĆ NA FLOW DIAGRAM w Lucid Chart

