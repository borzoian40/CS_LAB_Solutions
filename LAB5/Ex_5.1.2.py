"""
05.1.2 Noms des pays. French country names are feminine when they end with the letter
e, masculine otherwise, except for the following which are masculine even though they end
with e:
• le Belize
• le Cambodge
• le Mexique
• le Mozambique
• le Zaïre
• le Zimbabwe
Write a program that reads the French name of a country and adds the article: “le” for 
masculine or “la” for feminine, such as “le Canada” or “la Belgique”. 
However, if the country name starts with a vowel, use “l’”; for example, 
“l’Afghanistan”.
For the following plural country names, use “les”:
• les Etats-Unis
• les Pays-Bas
"""
def french_Country(name):
    country = ""
    if (name == "Belize" or   name == "Cambodge" or
                 name == "Mexique" or
                 name == "Mozambique" or
                 name == "Zaire" or
                 name == "Zimbawe"
    ):
        country = "le " + name
        print(country)
    elif name[-1] == "e":
        country = "la " + name
        print(country)
    elif (name[0] =="A" or name[0]  == "E" or
           name[0]  == "I" or name[0]  == "O" or name[0]  =="U"):
        country = "l'" + name
        print(country)
    elif (name == "United States" or name == "Netherlands"):
        country = "les " + name
        print(country)
    else:
        country = "le " + name
        print(country)


if __name__ == "__main__":
    country_name = input("Please enter the name of your country: ")
    french_Country(country_name)
