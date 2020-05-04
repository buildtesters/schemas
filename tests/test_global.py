import json
import os
import re
import pytest
import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def load_schema(path):
    """load a schema from file. We assume a json file
    """
    with open(path, "r") as fd:
        schema = json.loads(fd.read())
    return schema


def load_recipe(path):
    """load a yaml recipe file
    """
    with open(path, "r") as fd:
        content = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return content


def check_invalid_recipes(recipes, invalids, loaded):
    """This method validates all recipes found in tests/invalid/global with global schema: global/global.schema.json"""

    for recipe in recipes:
        assert recipe
        assert re.search("(yml|yaml)$", recipe)
        recipe_path = os.path.join(invalids, recipe)
        content = load_recipe(recipe_path)

        with pytest.raises(ValidationError) as excinfo:
            validate(instance=content, schema=loaded)
        print("Recipe File: %s  should be invalid" % recipe_path)


def check_valid_recipes(recipes, valids, loaded):
    """This method validates all recipes found in tests/valid/global with global schema: global/global.schema.json"""

    for recipe in recipes:
        assert recipe
        assert re.search("(yml|yaml)$", recipe)
        recipe_path = os.path.join(valids, recipe)
        content = load_recipe(recipe_path)

        validate(instance=content, schema=loaded)
        print("Recipe File: %s should be valid" % recipe_path)


def test_global_schema():
    """This test checks all field attributes in global.schema.json. The test ensures file exists and is
       able to load the schema. Once schema is loaded locally, each field is checked.
    """

    print("Root of testing is %s" % root)

    # Read in the outer validator (looks for list with keys and version)
    global_schema_file = os.path.join(root, "global", "global.schema.json")
    assert os.path.exists(global_schema_file)
    recipe = load_schema(global_schema_file)

    print("Testing global schema")
    # -------- check all fields ---------------------
    fields = [
        "$id",
        "$schema",
        "title",
        "type",
        "required",
        "propertyNames",
        "properties",
        "patternProperties",
    ]
    for field in fields:
        assert field in recipe

    assert (
        recipe["$id"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json"
    )
    assert recipe["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert recipe["type"] == "object"
    assert recipe["required"] == ["version"]

    # check propertyNames
    assert "pattern" in recipe["propertyNames"]
    assert recipe["propertyNames"]["pattern"] == "^[A-Za-z_][A-Za-z0-9_]*$"

    # check properties
    properties = recipe["properties"]
    assert "version" in properties
    assert "type" in properties["version"]
    assert properties["version"]["type"] == "string"

    # check patternProperties
    assert "type" in recipe["patternProperties"]["^[A-Za-z_.][A-Za-z0-9_]*$"]
    assert recipe["patternProperties"]["^[A-Za-z_.][A-Za-z0-9_]*$"]["type"] == [
        "object",
        "string",
    ]


def test_global_schema_examples():
    """This validates all valid/invalid examples for global schema"""
    global_schema_file = os.path.join(root, "global", "global.schema.json")
    loaded = load_schema(global_schema_file)

    invalid_dir = os.path.abspath(os.path.join(here, "invalid", "global"))
    valid_dir = os.path.abspath(os.path.join(here, "valid", "global"))

    invalid_recipes = os.listdir(invalid_dir)
    valid_recipes = os.listdir(valid_dir)

    assert invalid_recipes
    assert valid_recipes
    assert invalid_dir
    assert valid_dir
    assert loaded

    print(f"Detected Invalid Global Directory: {invalid_dir}")
    print(f"Detected Valid Global Directory: {valid_dir}")
    print(f"Invalid Recipes: {invalid_recipes}")
    print(f"Valid Recipes: {valid_recipes}")

    check_invalid_recipes(invalid_recipes, invalid_dir, loaded)
    check_valid_recipes(valid_recipes, valid_dir, loaded)
