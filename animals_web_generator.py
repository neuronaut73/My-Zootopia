import json


def load_data(file_name):
    """ Loads a JSON file """
    with open(file_name, "r") as handle:
        return json.load(handle)


def load_html(file_name):
    with open(file_name, "r") as handle:
        return handle.read()


def save_file(data: str, file_name: str):
    with open(file_name, "w") as f:
        return f.write(data)


def generate_string_with_animals_data(animals_data):
    output = ''  # define an empty string
    for dict in animals_data:
        name = dict["name"]
        location = dict["locations"][0]
        diet = dict["characteristics"]["diet"]
        type_fox = dict["characteristics"].get("type")

        variables = [name, location, diet, type_fox]
        print(variables)

        if all(var is not None for var in variables):
            output += '<li class="cards__item">'
            output += f"Name: {name}<br/>\n"
            output += f"Diet: {diet}<br/>\n"
            output += f"Location: {location}<br/>\n"
            output += f"Type: {type_fox}<br/>\n"
            output += '</li>'
    return output


def main():
    html_template = load_html("animals_template.html")
    animals_data = load_data('animals_data.json')
    animals_data_string = generate_string_with_animals_data(animals_data)
    html_template_new = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)
    save_file(html_template_new, "animals.html")


if __name__ == "__main__":
    main()


