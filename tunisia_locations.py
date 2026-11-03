"""Tunisia locations: Wilayat (Governorates) and Mo3tamdiyat (Delegations)."""

TUNISIA_LOCATIONS = {
    "Ariana": [
        "Ariana",
        "Raoued",
        "Kalaat El Andalous",
        "Skhira",
        "La Soukra"
    ],
    "Ben Arous": [
        "Ben Arous",
        "Rades",
        "Hammam-Lif",
        "Khalidia",
        "El Mourouj",
        "Mghira",
        "Fnaidha",
        "Bou Arada"
    ],
    "Bizerte": [
        "Bizerte",
        "Menzel Bourguiba",
        "Ras Jebel",
        "Bizerte Nord",
        "Bizerte Sud",
        "Mateur",
        "Menzel Jemil",
        "Tabarka",
        "Sejnane"
    ],
    "Gabès": [
        "Gabès Medina",
        "Gabès Nouvelle",
        "Metouia",
        "Matmata",
        "Mareth",
        "Ghannouch",
        "Chenini"
    ],
    "Gafsa": [
        "Gafsa",
        "Sened",
        "Mdhilla",
        "Redeyef",
        "Metlaoui",
        "Moularès",
        "El Ksar",
        "Oum El Araïs"
    ],
    "Jendouba": [
        "Jendouba",
        "Tabarka",
        "Ain Draham",
        "Ghardimaou",
        "Bou Arada",
        "Goubellat",
        "Nefza",
        "Fernana"
    ],
    "Kairouan": [
        "Kairouan",
        "El Ala",
        "Chebika",
        "Sbeitla",
        "Oueslatia",
        "Haffouz",
        "Sidi Bouz Zid",
        "Nasrallah",
        "Hajeb El Ayoun"
    ],
    "Kasserine": [
        "Kasserine",
        "Foussana",
        "Sbeitla",
        "Hichri",
        "Feriana",
        "Thala",
        "Hassi El Ferid",
        "Majel Bel Abbès",
        "Jedelienne"
    ],
    "Kebili": [
        "Kebili",
        "Douz",
        "Souk Lahad",
        "Zaafrane",
        "El Faouar"
    ],
    "Kef": [
        "Kef",
        "Tajerouine",
        "Sakiet Sidi Youssef",
        "Dahmani",
        "Jemna",
        "Kalaat Senhaja"
    ],
    "Mahdia": [
        "Mahdia",
        "Ksour Essaf",
        "Rejiche",
        "El Jem",
        "Chebba",
        "Skhira",
        "Ouled Chamekh"
    ],
    "Manouba": [
        "Manouba",
        "La Soukra",
        "Douar Hicher",
        "Oued Ellil",
        "Mornaguia",
        "Tébourba"
    ],
    "Medenine": [
        "Medenine",
        "Djerba Midoun",
        "Djerba Houmt Souk",
        "Ajim",
        "Ben Guerdane",
        "Skhira",
        "Zarzis",
        "El Ketf"
    ],
    "Monastir": [
        "Monastir",
        "Ksar Hellal",
        "Beni Hassan",
        "Jemmal",
        "Teboulba",
        "Sahline",
        "Ouerdanine",
        "Skhira"
    ],
    "Nabeul": [
        "Nabeul",
        "Hammamet",
        "Kelibia",
        "Menzel Temime",
        "Korba",
        "Dar Chaabane",
        "El Haouaria",
        "Menzel Horr",
        "Skhira"
    ],
    "Sfax": [
        "Sfax Medina",
        "Sfax Nouvelle",
        "Jebiniana",
        "Kerkennah",
        "Thyna",
        "Sakiet Ezzit",
        "Agareb",
        "Skhira",
        "El Mahrine"
    ],
    "Sidi Bouzid": [
        "Sidi Bouzid",
        "Regueb",
        "Mezzouna",
        "Bir El Hafey",
        "Sbikha",
        "Mnara"
    ],
    "Siliana": [
        "Siliana",
        "Kesra",
        "El Krib",
        "Rouhia",
        "Bargou",
        "Kossserine"
    ],
    "Sousse": [
        "Sousse Medina",
        "Sousse Riadh",
        "Akouda",
        "Kalaa Kebira",
        "Sahline",
        "Skhira",
        "El Djem",
        "Bouficha",
        "Enfida"
    ],
    "Tataouine": [
        "Tataouine",
        "Remada",
        "Dehiba",
        "Ghomrassen",
        "Ben Guerdane",
        "Foum Tataouine"
    ],
    "Tozeur": [
        "Tozeur",
        "Naftah",
        "Tamerza",
        "Degache",
        "Bled El Hadj"
    ],
    "Tunis": [
        "Tunis Medina",
        "Tunis Nouvelle Ville",
        "La Marsa",
        "Sidi Bou Saïd",
        "Carthage",
        "La Goulette",
        "Rades",
        "Ariana"
    ],
    "Zaghouan": [
        "Zaghouan",
        "Nadhour",
        "Skhira",
        "Saouaf",
        "Zriba",
        "El Fahs"
    ]
}


def get_wilayat() -> list:
    """Get list of all wilayat (governorates) in Tunisia."""
    return sorted(TUNISIA_LOCATIONS.keys())


def get_moatamdiyat(wilaya: str) -> list:
    """Get list of mo3tamdiyat (delegations) for a specific wilaya."""
    return sorted(TUNISIA_LOCATIONS.get(wilaya, []))


def get_all_locations() -> list:
    """Get all unique cities/delegations."""
    locations = set()
    for delegations in TUNISIA_LOCATIONS.values():
        locations.update(delegations)
    return sorted(locations)
