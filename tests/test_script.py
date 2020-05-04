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


def test_script_schema():
    """This test validates schema: script-v0.0.1.schema.json"""
    repo_prefix = "https://buildtesters.github.io/schemas"
    schema_name = "script"
    schema = "script-v0.0.1.schema.json"
    schema_file = os.path.join(root, schema_name, schema)
    # ensure schema file exists
    assert schema_file
    loaded = load_recipe(schema_file)
    # ensure load_recipe returns a dict object and not None
    assert isinstance(loaded, dict)

    # Checking schema fields
    fields = [
        "$id",
        "$schema",
        "title",
        "type",
        "propertyNames",
        "properties",
        "required",
    ]
    for field in fields:
        assert field in loaded

    # Check individual schema properties
    assert loaded["$id"] == "%s/%s/%s" % (repo_prefix, schema_name, schema)
    assert loaded["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert loaded["type"] == "object"
    assert loaded["propertyNames"] == {"pattern": "^[A-Za-z_][A-Za-z0-9_]*$"}
    assert loaded["type"] == "object"
    assert loaded["required"] == ["type", "run"]

    # check all properties keys
    found = [
        "type",
        "description",
        "maintainers",
        "env",
        "executor",
        "shell",
        "run",
        "status",
    ]
    print(f"Checking all keys: {found} in schema 'properties'")
    properties = loaded["properties"]

    for prop in found:
        print("Checking for property %s in %s" % (prop, schema_file))
        assert prop in properties

    # check all properties that are string types
    for section in ["type", "description", "shell", "shebang", "executor", "run"]:
        assert properties[section]["type"] == "string"

    # 'type' key takes a pattern string that must start and end with the word 'script'
    assert properties["type"]["pattern"] == "^script$"

    # check all properties that are object types
    assert properties["env"]["type"] == "object"
    assert properties["status"]["type"] == "object"

    # check all properties that are array types
    assert properties["maintainers"]["type"] == "array"

    assert "pattern" in properties["shell"]
    assert (
        loaded["properties"]["shell"]["pattern"]
        == "^(/bin/bash|/bin/sh|sh|bash|python).*"
    )

    # check status object
    status_properties = properties["status"]["properties"]
    assert "returncode" in status_properties
    assert "regex" in status_properties
    # regex has required fields for stream and exp, both must be defined
    assert "required" in status_properties["regex"]
    # check type for returncode and regex key
    assert status_properties["returncode"]["type"] == "integer"
    assert status_properties["regex"]["type"] == "object"

    status_regex_properties = status_properties["regex"]["properties"]
    # check for key 'stream' and 'exp' in regex object
    # check type for 'stream' and 'exp' key in regex object
    for item in ["stream", "exp"]:
        assert item in status_regex_properties
        assert status_regex_properties[item]["type"] == "string"


def test_script_examples(tmp_path):
    """the script test_organization is responsible for all the schemas
       in the root of the repository, under <schema>/examples.
       A schema specific test is intended to run tests that
       are specific to a schema. In this case, this is the "script"
       folder. Invalid examples should be under ./invalid/script.
    """
    print("Root of testing is %s" % root)

    schema_name = "script"
    schema_dir = os.path.abspath(os.path.join(root, schema_name))
    print("Testing schema %s" % schema_name)

    schemas = os.listdir(schema_dir)
    for schema in schemas:
        if schema.endswith("json"):

            # Assert it loads with jsonschema
            schema_file = os.path.join(schema_dir, schema)
            loaded = load_schema(schema_file)

            # Assert is named correctly
            print("Getting version of %s" % schema)
            match = re.search(
                "%s-v(?P<version>[0-9]{1}[.][0-9]{1}[.][0-9]{1})[.]schema[.]json"
                % schema_name,
                schema,
            )
            assert match

            # Ensure we found a version
            assert match.groups()
            version = match["version"]

            # Ensure a version folder exists with invalids
            print("Checking that invalids exist for %s" % schema)
            invalids = os.path.join(here, "invalid", schema_name, version)
            valids = os.path.join(here, "valid", schema_name, version)

            assert os.path.exists(invalids)
            invalid_recipes = os.listdir(invalids)
            valid_recipes = os.listdir(valids)

            assert invalid_recipes
            assert valid_recipes

            check_valid_recipes(valid_recipes, valids, loaded, version)
            check_invalid_recipes(invalid_recipes, invalids, loaded, version)
