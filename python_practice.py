#Lists:
#counties = ["Arapahoe","Denver","Jefferson"]
#counties.insert(2, "El Paso")
#counties.remove("El Paso")
#counties.pop(3)
#counties[2] = "El Paso"

#Tuples: 
#counties_tuple = ("Arapahoe","Denver","Jefferson") 
#counties_tuple[1]

#Dictionaries: 
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# counties_dict.items()
#counties_dict.keys()
#counties_dict.values()
#counties_dict.get("Denver")
#counties_dict['Arapahoe'] -or-
#counties_dict["Arapahoe"]

# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# #voting_data
# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")  
#for county in counties:
    #print(county)  
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county]) 

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)
# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# for key, value in counties_dict.items():
#     print(f"{key} county has {value:,} registered voters.")

# for value in voting_data:
#     print(value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):

#       print(voting_data[i])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:

#      print(county_dict['registered_voters'])

# for county_dict in voting_data:
#     print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.") 

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")


# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, 
{"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")




