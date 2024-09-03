import km_to_miles_converter

kilometers = float(input("Enter the KMs to change into miles: "))

km_to_miles = km_to_miles_converter.km_to_miles_converter(kilometers)

print(f"{kilometers} km is changed to {km_to_miles:.3f} miles!!")