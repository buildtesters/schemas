import json
import os
import pytest
import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(here))


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


def check_fields(recipe):
    # check json fields standard to most jsonschemas
    fields = [
        "$id",
        "$schema",
        "title",
        "type",
        "definitions",
        "properties",
        "additionalProperties",
        "required",
    ]
    for field in fields:
        assert field in recipe

    assert (
        recipe["$id"]
        == "https://HPC-buildtest.github.io/schemas/settings/settings.schema.json"
    )
    assert recipe["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert recipe["type"] == "object"
    assert recipe["required"] == ["editor", "executors"]
    assert recipe["additionalProperties"] == False


def check_properties(properties):
    # -------------------- check 'editor' key ------------------------------
    assert "editor" in properties
    assert "type" in properties["editor"]
    assert properties["editor"]["type"] == "string"
    assert "enum" in properties["editor"]
    assert properties["editor"]["enum"] == ["vi", "vim", "nano", "emacs"]

    # -------------------- check 'executors' key ------------------------------
    assert "executors" in properties
    assert "type" in properties["executors"]
    assert "patternProperties" in properties["executors"]
    assert "anyOf" in properties["executors"]["patternProperties"]["^.*$"]

    # check additionalProperties in properties
    assert "additionalProperties" in properties
    assert properties["additionalProperties"] == False


def check_definitions(definitions):

    # ------------------ check 'local' object ----------------------
    assert "local" in definitions
    assert "type" in definitions["local"]
    assert definitions["local"]["type"] == "object"
    assert "properties" in definitions["local"]
    assert "required" in definitions["local"]
    assert definitions["local"]["required"] == ["type"]

    local_properties = definitions["local"]["properties"]
    # ------------ check 'description' -----------------------
    assert "description" in local_properties
    assert "type" in local_properties["description"]
    assert local_properties["description"]["type"] == "string"

    # ------------ check 'type' -----------------------
    assert "type" in local_properties
    assert "type" in local_properties["type"]
    assert local_properties["type"]["type"] == "string"

    assert "enum" in local_properties["type"]
    assert local_properties["type"]["enum"] == ["local"]

    # ------------ check 'options' -----------------------
    assert "options" in local_properties
    assert "type" in local_properties["options"]
    assert local_properties["options"]["type"] == "array"
    assert "items" in local_properties["options"]
    assert "type" in local_properties["options"]["items"]
    assert local_properties["options"]["items"]["type"] == "string"

    # ------------------ check 'slurm' object ----------------------

    assert "slurm" in definitions
    assert "type" in definitions["slurm"]
    assert definitions["slurm"]["type"] == "object"
    assert "properties" in definitions["slurm"]
    assert "required" in definitions["slurm"]
    assert definitions["slurm"]["required"] == ["type", "launcher"]
    # ------------------ check 'slurm' properties ----------------------
    slurm_properties = definitions["slurm"]["properties"]
    # ------------------ check 'description' in slurm properties ----------------------
    assert "description" in slurm_properties
    assert "type" in slurm_properties["description"]
    assert slurm_properties["description"]["type"] == "string"
    # ------------------ check 'type' in slurm properties ----------------------
    assert "type" in slurm_properties
    assert "type" in slurm_properties["type"]
    assert slurm_properties["type"]["type"] == "string"
    assert "enum" in slurm_properties["type"]
    assert slurm_properties["type"]["enum"] == ["slurm"]

    # ------------------ check 'launcher' in slurm properties ----------------------
    assert "launcher" in slurm_properties
    assert "type" in slurm_properties["launcher"]
    assert slurm_properties["launcher"]["type"] == "string"
    assert "enum" in slurm_properties["launcher"]
    assert slurm_properties["launcher"]["enum"] == ["sbatch"]

    # ------------------ check 'options' in slurm properties ----------------------

    assert "options" in slurm_properties
    assert "type" in slurm_properties["options"]
    assert slurm_properties["options"]["type"] == "array"
    assert "items" in slurm_properties["options"]
    assert "type" in slurm_properties["options"]["items"]
    assert slurm_properties["options"]["items"]["type"] == "string"


def test_settings():

    settings_schema = os.path.join(root, "settings", "settings.schema.json")
    # check if file exists
    assert settings_schema

    # load schema and ensure type is a dict
    recipe = load_schema(settings_schema)
    assert isinstance(recipe, dict)

    check_fields(recipe)
    check_properties(recipe["properties"])
    check_definitions(recipe["definitions"])

    valid_recipes = os.path.join(root, "settings", "valid")
    invalid_recipes = os.path.join(root, "settings", "invalid")

    # check all valid recipes
    for example in os.listdir(valid_recipes):
        filepath = os.path.join(valid_recipes, example)
        print(f"Loading Recipe File: {filepath}")
        example_recipe = load_recipe(filepath)
        assert example_recipe

        print(f"Expecting Recipe File: {filepath} to be valid")
        validate(instance=example_recipe, schema=recipe)

    # check all valid recipes
    for example in os.listdir(invalid_recipes):
        filepath = os.path.join(invalid_recipes, example)
        print(f"Loading Recipe File: {filepath}")
        example_recipe = load_recipe(filepath)
        assert example_recipe

        print(f"Expecting Recipe File: {filepath} to be invalid")
        with pytest.raises(ValidationError) as excinfo:
            validate(instance=example_recipe, schema=recipe)
