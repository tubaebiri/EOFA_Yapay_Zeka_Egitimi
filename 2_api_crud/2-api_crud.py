import requests

countries=[]
#api'den veri çekme fonksiyonu
def get_countries():
    try:
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for country in data:
                country_info = {
                    "name": country["name"]["common"],
                    "capital": country.get("capital", ["Bilinmiyor"])[0],  
                    "region": country.get("region", "Bilinmiyor"),        
                    "population": country.get("population", 0)             
                }
                countries.append(country_info)
            print("Ülkeler başarıyla alındı")
        else:
            print("Hata! Ülkeler alınamadı")
    except:
        print("Bir hata oluştu, internet bağlantınızı kontrol edin")

#ulke ekleme fonksiyonu
def add_country(country_name):
    new_country = {
        "name": country_name,
        "capital": "Bilinmiyor",
        "region": "Bilinmiyor",
        "population": 0
    }
    countries.append(new_country)
    print(f"{country_name} başarıyla eklendi")

#ülke güncelleme fonksiyonu
def update_country(country_name, new_info):
    for country in countries:
        if country["name"].lower() == country_name.lower():
            country.update(new_info)
            print(f"{country_name} güncellendi")
            return
    print(f"{country_name} bulunamadı")

#ulke silme fonksiyonu 
def delete_country(country_name):
    for country in countries:
        if country["name"].lower() == country_name.lower():
            countries.remove(country)
            print(f"{country_name} silindi")
            return
    print(f"{country_name} bulunamadı")

# nüfusa göre filtreleme fonksiyonu 
def filter_by_population(min_population):
    result = []
    for country in countries:
        if country["population"] >= min_population:
            result.append(country)
    return result

# bölgeye göre filtreleme fonksiyonu
def filter_by_region(region):
    result = []
    for country in countries:
        if country["region"].lower() == region.lower():
            result.append(country)
    return result

# baskente göre arama fonksiyonu
def search_by_capital(capital):
    result = []
    for country in countries:
        if capital.lower() in country["capital"].lower():
            result.append(country)
    return result

get_countries()

add_country("ornekulke")

update_country("Turkey", {"population": 84000000})

print("\nNüfusu 50 milyondan fazla olan ülkeler:")
big_countries = filter_by_population(50000000)
for country in big_countries[:5]:
    print(f"{country['name']}: {country['population']}")

print("\nAvrupa'daki ülkeler:")
european_countries = filter_by_region("Europe")
for country in european_countries[:5]:
    print(f"{country['name']}")

print("\nBaşkenti Paris olan ülke:", search_by_capital("paris"))

delete_country("Italy")