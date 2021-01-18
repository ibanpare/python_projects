import requests
import bs4

"""
City CAN TAKE FROM QUERY
Neighborhood NA
Zipcode  CAN TAKE FROM QUERY
# of Baths NA IN SEARCH
Sqft NA IN SEARCH

"""

#headers needed to avoid blocking

headers = {
    'authority': 'www.apartments.com',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


def query_url():
    """
    query takes:
    'town-state' will convert even if spaces instead of dashes and uppercase
    will take ny neighbourhoods
    'town-state-zipcode' e.g. new-york-ny-10001
    """
    home_url = "https://www.apartments.com/"
    town = input("Insert your town: ")
    state = input("Insert your state, e.g. CA for California: ")
    while True:
        alsozip = input("Do you want to add a ZIP code? (y or n) ")
        if alsozip.lower() == "y":
            zipcode = input("Type your ZIP code: ")
            full_url = home_url + f"{town}-{state}-{zipcode}"
            return full_url
        elif alsozip.lower() == "n":
            full_url = home_url + f"{town}-{state}"
            return full_url
        else:
            continue

res = requests.get(query_url(),  headers=headers)
soup = bs4.BeautifulSoup(res.content, "lxml")

apartment_name = soup.find(class_="js-placardTitle title")
apartment_address = soup.find(class_="property-address js-url")
number_of_beds = soup.find(class_="bed-range")
rent = soup.find(class_="price-range")
amenities = soup.find(class_="property-amenities")
apartment_url = soup.find("a", class_="property-link")

print()
print(f"Page title is {soup.title.text}")
print()
print(f"First apartment name: {apartment_name.text}")
print()
print(f"First apartment address: {apartment_address.text}")
print(f"Number of beds: {number_of_beds.text}")
print(f"Rent: {rent.text}")
print(f"Amenities: {amenities.text}")
print(f"Url: {apartment_url['href']}")
