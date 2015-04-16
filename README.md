# częśc demonstracyjna (pośrednictwo handlu płodami rolnymi rolnik-konsument)
- (http://www.klasyfikacje.gofin.pl/pkwiu/1,2,2,produkty-rolnictwa-i-lowiectwa-oraz-uslugi-wspomagajace.html#D01)
- rolnik
    - rejestracja
        - profil
            - adres
            - panel administracyjny do zmiany danych
              - cms (wiadomości pisane prszez administrację serwisu dla rolników)

- konsument
- dostęp otwarty
    - mapy z geograficznym wyszukiwaniem
        - odległość jako parametr 
    - wskazywanie profilu (czego szukam)
    - interfejs reaktywny (dostoswuje się do rozdzielczości urządzenia)

- 1.6 -> 1.8
    - przy zmianach modeli: ```manage.py makemigrations
      manage.py migrate```
        - po pchnięciu na serwer: ```git> migrate-apps-db plodyrolne```
    - używajmy ```{% url 'nazwa_urla' %}``` bo aplikacja jest w subfolderze
	- Django jęczy na foreignkey(unique=True). Powstało [OneToOneField](https://docs.djangoproject.com/en/1.8/ref/models/fields/#ref-onetoone)
