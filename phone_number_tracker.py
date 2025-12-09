import phonenumbers
from phonenumbers import geocoder, carrier

# Take phone number input
number = input("Enter phone number with country code (e.g. +918123456789): ")

try:
    parsed_number = phonenumbers.parse(number)

    # Get country / region
    location = geocoder.description_for_number(parsed_number, "en")

    # Get carrier
    sim_carrier = carrier.name_for_number(parsed_number, "en")

    print("Location:", location)
    print("Carrier:", sim_carrier)

except:
    print("Invalid phone number!")
