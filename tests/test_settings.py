import json
import os
import yaml
from jsonschema import validate

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
schemaroot = os.path.join(os.path.dirname(here), "schemas")

schema_file = "settings.schema.json"
settings_schema = os.path.join(schemaroot, schema_file)


def load_schema(path):
    """load a schema from file. We assume a json file"""
    with open(path, "r") as fd:
        schema = json.loads(fd.read())
    return schema


def load_recipe(path):
    """load a yaml recipe file"""
    with open(path, "r") as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content


def test_settings_examples():

    # load schema and ensure type is a dict
    recipe = load_schema(settings_schema)

    valid = os.path.join(root, "settings", "valid")
    assert valid

    valid_recipes = os.listdir(valid)
    assert valid_recipes
    # check all valid recipes
    for example in valid_recipes:

        filepath = os.path.join(valid, example)
        print(f"Loading Recipe File: {filepath}")
        example_recipe = load_recipe(filepath)
        assert example_recipe

        print(f"Expecting Recipe File: {filepath} to be valid")
        validate(instance=example_recipe, schema=recipe)
