import json
import os
import pytest
import re
import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)

schema_name = "compiler"
schema_file = f"{schema_name}-v1.0.schema.json"
schema_path = os.path.join(root, schema_name, schema_file)


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


def check_invalid_recipes(recipes, invalids, loaded, version):
    for recipe in recipes:
        assert recipe
        assert re.search("(yml|yaml)$", recipe)
        recipe_path = os.path.join(invalids, recipe)
        content = load_recipe(recipe_path)

        # Ensure version is correct in header
        assert content["version"] == version
        del content["version"]

        # For each section, assume folder type and validate
        for name in content.keys():
            with pytest.raises(ValidationError) as excinfo:
                validate(instance=content[name], schema=loaded)
            print(excinfo.type, excinfo.value)
            print("Testing %s from recipe %s should be invalid" % (name, recipe))


def check_valid_recipes(recipes, valids, loaded, version):
    for recipe in recipes:
        assert recipe
        assert re.search("(yml|yaml)$", recipe)
        recipe_path = os.path.join(valids, recipe)
        content = load_recipe(recipe_path)

        # Ensure version is correct in header
        assert content["version"] == version
        del content["version"]

        # For each section, assume folder type and validate
        for name in content.keys():
            validate(instance=content[name], schema=loaded)
            print("Testing %s from recipe %s should be valid" % (name, recipe))


def test_compiler_schema():

    assert schema_path
    recipe = load_recipe(schema_path)
    assert isinstance(recipe, dict)

    fields = [
        "$id",
        "$schema",
        "title",
        "type",
        "propertyNames",
        "properties",
        "additionalProperties",
        "required",
    ]
    for field in fields:
        assert field in recipe

    assert (
        recipe["$id"]
        == "https://buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json"
    )
    assert recipe["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert recipe["type"] == "object"
    assert recipe["required"] == ["type", "compiler", "executor"]
    assert recipe["propertyNames"]["pattern"] == "^[A-Za-z_][A-Za-z0-9_]*$"
    assert recipe["additionalProperties"] == False

    properties = recipe["properties"]

    # check type and description key and type
    for key in ["type", "description"]:
        assert properties[key]["type"] == "string"

    assert properties["type"]["pattern"] == "^compiler$"

    # check module key
    assert properties["module"]["type"] == "array"
    assert properties["module"]["items"]["type"] == "string"

    assert (
        properties["executor"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/executor"
    )
    assert (
        properties["sbatch"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/sbatch"
    )
    assert (
        properties["env"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert (
        properties["vars"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert properties["compiler"]["type"] == "object"
    assert properties["compiler"]["additionalProperties"] == False
    # check compiler properties
    assert properties["compiler"]["required"] == ["source", "name"]

    compiler_properties = properties["compiler"]["properties"]
    for key in [
        "name",
        "source",
        "exec_args",
        "cflags",
        "cxxflags",
        "fflags",
        "cppflags",
        "ldflags",
    ]:
        assert compiler_properties[key]["type"] == "string"

    compiler_properties["name"]["enum"] == ["gnu", "intel", "pgi", "cray"]


def test_compiler_schema_examples():

    print(root)

    loaded = load_schema(schema_path)
    assert isinstance(loaded, dict)

    # Assert is named correctly
    print("Getting version of %s" % schema_file)
    match = re.search(
        "%s-v(?P<version>[0-9]{1}[.][0-9]{1})[.]schema[.]json" % schema_name,
        schema_file,
    )
    print(match)
    assert match

    # Ensure we found a version
    assert match.groups()
    version = match["version"]

    invalids = os.path.join(here, "invalid", schema_name, version)
    valids = os.path.join(here, "valid", schema_name, version)

    assert invalids
    assert valids

    invalid_recipes = os.listdir(invalids)
    valid_recipes = os.listdir(valids)

    assert invalid_recipes
    assert valid_recipes

    # check_invalid_recipes(invalid_recipes, invalids, loaded, version)
    check_valid_recipes(valid_recipes, valids, loaded, version)
