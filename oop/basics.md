# OOP

## Zasady programowania obiektowego

1. Abstraction - zamknięcie złożonej logiki za prostym interfejsem (np. pilot do telewizora)
2. Inheritance - kopiowanie metod i pól klas rodziców. 
   - Dziedziczenie horyzontalne i wertykalne. 
   - Używa się do specjalizacji klasy bazowej
   - Algorytm C3 lub linearyzacja dziedziczenia (pierwsze w MRO). 
3. Polymorphism - różne zachowanie metody w zależności od kontekstu wywołania
4. Encapsulation - ograniczenie dostępu za pomocą access modifiers (w pythonie nie ma). 
Ale też np. stworzenie klasy (przestrzeni nazewniczej) celem ograniczenia dostępu do pól i metod.
Access modifiers: 
   - private (tylko w danej klasie `__name`, nie używa się w pythonie ze względu na name mangling), 
   - protected (tylko w klasie i klasach dziedziczących, `_name`), 
   - public (ogólnie dostępny, `name`)
   - read only (stała, `NAME`)

## SOLID - zestaw dobrych praktyk OOP

1. Single Responsibility Principle - klasa powinna zajmować się tylko jedną rzeczą. 
2. Open/Closed Principle - klasa zamknięta na modyfikacje, otwarta na dziedziczenie. 
   - nie modyfikuje się, bo mogłoby dojść do uszkodzenia klas dziedziczących.
3. Liskov Substitution Principle - dowolny obiekt klasy dziedziczącej podstawiony w miejsce obiektu klasy bazowej nie powinien zmieniać działania programu
   - chodzi o to, żeby za bardzo nie odbiegać od pierwotnej idei obiektu
4. Interface Segregation Principle - odseparowanie logiki od szczegółu implementacyjnego
   - w pythonie klasy abstrakcyjne 
   - zbiór zasad, które definiują obiekt, ale muszą zostać zaimplementowane w klasach dziedziczących
5. Dependency Inverstion Principle - klasa rodzica nie może być zależna od dziecka 
   - np. klasa bazowa odnosi się do pól klas dziedziczących, to wtedy staje się od nich zależna


## Słownik

1. Klasa - namespace (przestrzeń nazewnicza) dla zmiennych i funkcji (pól i metod)
2. Obiekt - instancja klasy, posiada pola i dostęp do funkcjonalności 
   - w pythonie obiekt ma pola, ale metody są trzymane w klasie 
3. Pole - attribute/property - zarówno zmienne, jak i funkcje 
   - pola klasy - współdzielone przez wszystkie instancje i klasy w drzewie dziedziczenia
   - pola obiektu - zmienna w kontekście obiektu, każdy obiekt na swoją wartość (tworzenie: `self.value = value`), 
   tworzone w `__init__`, bo mamy gwarancję, że będą w obiekcie, bo przy tworzeniu przez metodę może być różnie
4. Metoda - funkcja w kontekście klasy (bo to klasy trzymają metody!)
   - metody z self - służą do manipulowania obiektem
   - @staticmethod - rodzaj metody statycznej, nie potrzebują obiektu, żeby dało się je wywołać; nie mają selfa więc nie mogą manipulować obiektem ani klasą, każda mogłaby być zewnętrzną funkcją, ale skoro logicznie pasuje, to OK
   - @classmethod - rodzaj metody statycznej; przyjmują obiekt klasy (cls), służy do interakcji z klasą (np. jako custom constructor), np. `__new__` to jest de facto class method
5. Konstruktor - metoda tworząca obiekt `__new__`
   - uwaga - `__init__` przyjmuje jako pierwszy obiekt self, który musiał zostać wcześniej stworzony
   - tylko metoda `__new__` klasy object może de facto utworzyć obiekt 
6. self - obiekt powstały na podstawie klasy, w której jest zdefiniowany 
7. Data Object Descriptor and Object Descriptor - klasa, która ma zaimplementowany protokół Descriptor (get, set, del)
   - tylko getter -> object descriptor
   - setter + getter -> data object descriptor
   - najbardziej znana klasa: property
   - używane do ograniczenia dostępu/wystawienia API obiektu (ale nie w pythonie)
   - getter używany do formatowania, setter do walidacji
   - setter jest bindowany do obiektu gettera, więc nie da się go stworzyć bez gettera
8. Metaklasa - klasa służąca do tworzenia klas (tj. instancją klasy jest klasa)
9. Klasa abstrakcyjna - klasa, które nie da się sensownie zainstancjonować 
   - wymusza na concrete class implementację swojej zawartości, sama może mieć częściową implementację
   - używane w Interface Segregation Principle, ale w pythonie nie ma interfejsów
10. super() - metaklasa implementująca wzorzez projektowy Proxy (tj. opakowanie obiektu, żeby ograniczyć dostęp, rozszerzyć funkcjonalność)
   - przewija poziom dziedziczenia (MRO) o jeden poziom do góry
11. Kolejność wywoływania dunder methods:
    - `__new__` konstruktor tworzy obiekt, przekazuje do init
    - `__init__` tworzy nowe pola obiektu, ale nic nie zwraca
    - `__call__` wywołanie (każdy obiekt można uczynić wywoływalnym)
    - 