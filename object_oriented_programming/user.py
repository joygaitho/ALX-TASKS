import json

def process_json(data: dict, filename: str) -> dict:
    """
    Serializes a Python dictionary to a JSON file and then deserializes 
    the file content back into a Python dictionary.

    Args:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        dict: The dictionary deserialized from the JSON file.
    """
    # 1. Serialization (Python dict -> JSON file)
    # The 'w' mode means "write" (creates the file or overwrites it)

    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
            print(f"Successfull serialized data to '{filename}'")
    except IOError as e:
        print(f"Error during serialization: {e}")
        return {} # return an empty dict on file error

# 2. Deserialization (JSON file -> Python dict)
    # The 'r' mode means "read"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Successfully deserialized data from '{filename}'")
            return data
    except FileNotFoundError as e:
        print(f"Error! File '{filename}' not found during deserialization: {e}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error in deserialization: Invalid JSON format in file: {e}")
        return {}
    
    # define input data (python dictionary)

person_data = {"full_name": "Maya Hawke", "age": 23, "nationality": "American", "roles": ["Actress, Singer"]}

new_data = process_json(person_data, "user.json") # fucntion call

print(f"Original type: {type(person_data)}")
print(f"Returned type: {type(new_data)}")
print(f"Returned data: {new_data}")

# additional info
# data: dict hints that the function expects the data argument to be a dictionary.

# -> dict hints that the function is expected to return a dictionary.