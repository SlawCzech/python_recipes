# Iterable

class CustomIterable:
    def __init__(self, start, stop, step):
        self._data = list(range(start, stop, step))

    def __iter__(self):
        return iter(self._data)


fancy_collection = CustomIterable(1, 10, 2)


# print(fancy_collection)

# for item in fancy_collection:
#     print(item)


# print(iter(fancy_collection))

# iterator definiuje który element będzie następny, dlatego może być customowy, tj. iterator to nie iterable!!

class Array:
    def __init__(self, iterator):
        self._data = list(range(11))
        self._iterator = iterator

    def __iter__(self):
        return self._iterator(self._data)


class EveryThird:
    def __init__(self, data):
        self._data = data
        self._counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._data) <= self._counter:
            raise StopIteration

        result = self._data[self._counter]
        self._counter += 3
        return result


class Odd:
    def __init__(self, data):
        self._data = data
        self._counter = 0

    def __iter__(self):
        return iter(self)

    def __next__(self):
        if len(self._data) <= self._counter:
            raise StopIteration

        for item in self._data[self._counter:]:
            self._counter += 1
            if item % 2 != 0:
                return item

        raise StopIteration  # jak już nie ma elementów w pętli


every_third_items = Array(EveryThird)

odd_items = Array(Odd)

# for item in every_third_items:
#     print(item)
#
# print('x' * 20)
# print()
# print('x' * 20)

# for item in odd_items:
#     print(item)

# wrócić do trawersowania po drzewach binarnych!!!!!


world = {
    "Africa": {
        "Algeria": "Algiers",
        "Angola": "Luanda",
        "Benin": "Porto-Novo",
        "Botswana": "Gaborone",
        "Burkina Faso": "Ouagadougou",
        "Burundi": "Bujumbura",
        "Cabo Verde": "Praia",
        "Cameroon": "Yaounde",
        "Central African Republic": "Bangui",
        "Chad": "N'Djamena",
        "Comoros": "Moroni",
        "Congo": "Brazzaville",
        "Cote d'Ivoire": "Yamoussoukro",
        "Democratic Republic of the Congo": "Kinshasa",
        "Djibouti": "Djibouti",
        "Egypt": "Cairo",
        "Equatorial Guinea": "Malabo",
        "Eritrea": "Asmara",
        "Eswatini": "Mbabane",
        "Ethiopia": "Addis Ababa",
        "Gabon": "Libreville",
        "Gambia": "Banjul",
        "Ghana": "Accra",
        "Guinea": "Conakry",
        "Guinea-Bissau": "Bissau",
        "Kenya": "Nairobi",
        "Lesotho": "Maseru",
        "Liberia": "Monrovia",
        "Libya": "Tripoli",
        "Madagascar": "Antananarivo",
        "Malawi": "Lilongwe",
        "Mali": "Bamako",
        "Mauritania": "Nouakchott",
        "Mauritius": "Port Louis",
        "Morocco": "Rabat",
        "Mozambique": "Maputo",
        "Namibia": "Windhoek",
        "Niger": "Niamey",
        "Nigeria": "Abuja",
        "Rwanda": "Kigali",
        "Sao Tome and Principe": "Sao Tome",
        "Senegal": "Dakar",
        "Seychelles": "Victoria",
        "Sierra Leone": "Freetown",
        "Somalia": "Mogadishu",
        "South Africa": "Pretoria",
        "South Sudan": "Juba",
        "Sudan": "Khartoum",
        "Tanzania": "Dodoma",
        "Togo": "Lome",
        "Tunisia": "Tunis",
        "Uganda": "Kampala",
        "Zambia": "Lusaka",
        "Zimbabwe": "Harare"
    },
    "Asia": {
        "Afghanistan": "Kabul",
        "Bahrain": "Manama",
        "Bangladesh": "Dhaka",
        "Bhutan": "Thimphu",
        "Brunei": "Bandar Seri Begawan",
        "Cambodia": "Phnom Penh",
        "China": "Beijing",
        "Cyprus": "Nicosia",
        "East Timor": "Dili",
        "India": "New Delhi",
        "Indonesia": "Jakarta",
        "Iran": "Tehran",
        "Iraq": "Baghdad",
        "Israel": "Jerusalem",
        "Japan": "Tokyo",
        "Jordan": "Amman",
        "Kazakhstan": "Nur-Sultan",
        "Kuwait": "Kuwait City",
        "Kyrgyzstan": "Bishkek",
        "Laos": "Vientiane",
        "Lebanon": "Beirut",
        "Malaysia": "Kuala Lumpur",
        "Maldives": "Male",
        "Mongolia": "Ulaanbaatar",
        "Myanmar": "Naypyidaw",
        "Nepal": "Kathmandu",
        "North Korea": "Pyongyang",
        "Oman": "Muscat",
        "Pakistan": "Islamabad",
        "Palestine": "Ramallah",
        "Philippines": "Manila",
        "Qatar": "Doha",
        "Saudi Arabia": "Riyadh",
        "Singapore": "Singapore",
        "South Korea": "Seoul",
        "Sri Lanka": "Colombo",
        "Syria": "Damascus",
        "Taiwan": "Taipei",
        "Tajikistan": "Dushanbe",
        "Thailand": "Bangkok",
        "Turkey": "Ankara",
        "Turkmenistan": "Ashgabat",
        "United Arab Emirates": "Abu Dhabi",
        "Uzbekistan": "Tashkent",
        "Vietnam": "Hanoi",
        "Yemen": "Sana'a"
    },
    "Europe": {
        "Albania": "Tirana",
        "Andorra": "Andorra la Vella",
        "Armenia": "Yerevan",
        "Austria": "Vienna",
        "Azerbaijan": "Baku",
        "Belarus": "Minsk",
        "Belgium": "Brussels",
        "Bosnia and Herzegovina": "Sarajevo",
        "Bulgaria": "Sofia",
        "Croatia": "Zagreb",
        "Cyprus": "Nicosia",
        "Czech Republic": "Prague",
        "Denmark": "Copenhagen",
        "Estonia": "Tallinn",
        "Finland": "Helsinki",
        "France": "Paris",
        "Georgia": "Tbilisi",
        "Germany": "Berlin",
        "Greece": "Athens",
        "Hungary": "Budapest",
        "Iceland": "Reykjavik",
        "Ireland": "Dublin",
        "Italy": "Rome",
        "Kazakhstan": "Nur-Sultan",
        "Kosovo": "Pristina",
        "Latvia": "Riga",
        "Liechtenstein": "Vaduz",
        "Lithuania": "Vilnius",
        "Luxembourg": "Luxembourg",
        "Malta": "Valletta",
        "Moldova": "Chisinau",
        "Monaco": "Monaco",
        "Montenegro": "Podgorica",
        "Netherlands": "Amsterdam",
        "North Macedonia": "Skopje",
        "Norway": "Oslo",
        "Poland": "Warsaw",
        "Portugal": "Lisbon",
        "Romania": "Bucharest",
        "Russia": "Moscow",
        "San Marino": "San Marino",
        "Serbia": "Belgrade",
        "Slovakia": "Bratislava",
        "Slovenia": "Ljubljana",
        "Spain": "Madrid",
        "Sweden": "Stockholm",
        "Switzerland": "Bern",
        "Turkey": "Ankara",
        "Ukraine": "Kyiv",
        "United Kingdom": "London",
        "Vatican City": "Vatican City"
    },
    "North America": {
        "Antigua and Barbuda": "St. John's",
        "Bahamas": "Nassau",
        "Barbados": "Bridgetown",
        "Belize": "Belmopan",
        "Canada": "Ottawa",
        "Costa Rica": "San Jose",
        "Cuba": "Havana",
        "Dominica": "Roseau",
        "Dominican Republic": "Santo Domingo",
        "El Salvador": "San Salvador",
        "Grenada": "St. George's",
        "Guatemala": "Guatemala City",
        "Haiti": "Port-au-Prince",
        "Honduras": "Tegucigalpa",
        "Jamaica": "Kingston",
        "Mexico": "Mexico City",
        "Nicaragua": "Managua",
        "Panama": "Panama City",
        "Saint Kitts and Nevis": "Basseterre",
        "Saint Lucia": "Castries",
        "Saint Vincent and the Grenadines": "Kingstown",
        "Trinidad and Tobago": "Port of Spain",
        "United States": "Washington, D.C."
    },
    "Oceania": {
        "Australia": "Canberra",
        "Fiji": "Suva",
        "Kiribati": "Tarawa",
        "Marshall Islands": "Majuro",
        "Micronesia": "Palikir",
        "Nauru": "Yaren",
        "New Zealand": "Wellington",
        "Palau": "Ngerulmud",
        "Papua New Guinea": "Port Moresby",
        "Samoa": "Apia",
        "Solomon Islands": "Honiara",
        "Tonga": "Nuku'alofa",
        "Tuvalu": "Funafuti",
        "Vanuatu": "Port Vila"
    },
    "South America": {
        "Argentina": "Buenos Aires",
        "Bolivia": "La Paz",
        "Brazil": "Brasilia",
        "Chile": "Santiago",
        "Colombia": "Bogota",
        "Ecuador": "Quito",
        "Guyana": "Georgetown",
        "Paraguay": "Asuncion",
        "Peru": "Lima",
        "Suriname": "Paramaribo",
        "Uruguay": "Montevideo",
        "Venezuela": "Caracas"
    }
}


# iterator zwracający stolice alfabetycznie

class Capitals:
    def __init__(self, data):
        self._capitals = self._retrieve_data(data)
        self._index = 0

    @staticmethod
    def _retrieve_data(data):
        capitals = []
        for countries in data.values():
            for capital in countries.values():
                capitals.append(capital)
        return sorted(capitals)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._capitals) <= self._index:
            raise StopIteration

        result = self._capitals[self._index]
        self._index += 1
        return result


capitals_ = Capitals(world)

# print(next(capitals_))
# print(next(capitals_))
# print(next(capitals_))