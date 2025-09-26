# Dictionary
capital = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
# List
alphabet = ["A","B","C"]

# Nested list with dictionary
travel_log1 = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"]
}
print(travel_log1["France"][1])

# Nested List
nested_list = ["A","B",["C",'D']]
print(nested_list[2])
print(nested_list[2][1])

# Nested Dictionary
nested_dictionary = {
    "Person 1" : "Joe Goldberg",
    "Person 2" : {
        "Devil" : "Lucifer Morningstar",
        "Daughter": "Sabrina Morningstar"
    }
}
print(nested_dictionary["Person 1"])
print(nested_dictionary["Person 2"])
print(nested_dictionary["Person 2"]["Devil"])

# Nested list with dictionary 2
travel_log = {
    "France" : {
       "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visites" : 12
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5
    }
}
print(travel_log["Germany"]["cities_visited"][2])