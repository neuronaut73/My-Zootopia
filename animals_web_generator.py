import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')


output = ''  # define an empty string
for dict in animals_data:
    name = dict["name"]
    location = dict["locations"][0]
    diet = dict["characteristics"]["diet"]
    type_fox = dict["characteristics"].get("type")

    variables = [name, location, diet, type_fox]

    if all(var is not None for var in variables):
        # append information to each string
        output += f"Name: {name}\n"
        output += f"Diet: {diet}\n"
        output += f"Location: {location}\n"
        output += f"Type: {type_fox}\n"

print(output)



