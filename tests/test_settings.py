import json
import os
import yaml
from jsonschema import validate

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


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
        == "https://buildtesters.github.io/schemas/settings/settings.schema.json"
    )
    assert recipe["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert recipe["type"] == "object"
    assert recipe["required"] == ["config", "executors"]
    assert recipe["additionalProperties"] == False


def check_properties(properties):

    # check additionalProperties in properties
    assert properties["additionalProperties"] == False

    # -------------------- check 'executors' key ------------------------------
    assert "executors" in properties
    assert properties["executors"]["type"] == "object"

    assert "properties" in properties["executors"]
    executor_properties = properties["executors"]["properties"]
    assert properties["executors"]["additionalProperties"] == False

    for key in ["local", "ssh", "slurm"]:
        assert key in executor_properties
        assert executor_properties[key]["type"] == "object"
        assert executor_properties[key]["patternProperties"]["^.*$"]
        if key == "local":
            assert (
                executor_properties[key]["patternProperties"]["^.*$"]["$ref"]
                == "#/definitions/local"
            )
        elif key == "slurm":
            assert (
                executor_properties[key]["patternProperties"]["^.*$"]["$ref"]
                == "#/definitions/slurm"
            )
        else:
            assert (
                executor_properties[key]["patternProperties"]["^.*$"]["$ref"]
                == "#/definitions/ssh"
            )

    # check config property
    assert "config" in properties
    config_section = properties["config"]
    assert config_section["type"] == "object"
    assert config_section["additionalProperties"] == False

    assert "properties" in config_section
    config_properties = config_section["properties"]
    # -------------------- check 'editor' key ------------------------------
    assert config_properties["editor"]["type"] == "string"
    assert config_properties["editor"]["enum"] == ["vi", "vim", "nano", "emacs"]
    assert config_properties["editor"]["default"] == "vim"

    assert "paths" in config_properties
    config_path_properties = config_properties["paths"]
    assert config_path_properties["type"] == "object"

    for key in ["prefix", "logdir", "clonepath", "testdir"]:
        assert config_path_properties["properties"][key]["type"] == "string"


def check_definitions(definitions):

    # ------------------ check 'local' object ----------------------
    assert "local" in definitions
    assert definitions["local"]["type"] == "object"
    assert definitions["local"]["additionalProperties"] == False

    local_properties = definitions["local"]["properties"]

    assert local_properties["description"]["type"] == "string"
    assert local_properties["shell"]["type"] == "string"
    assert (
        local_properties["environment"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert (
        local_properties["variables"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert local_properties["retry"]["type"] == "integer"
    assert local_properties["retry"]["minimum"] == 1
    assert local_properties["retry"]["maximum"] == 5
    assert local_properties["modules"]["$ref"] == "#/definitions/modules"

    # ------------------ check 'slurm' object ----------------------

    assert "slurm" in definitions
    assert definitions["slurm"]["type"] == "object"
    assert definitions["slurm"]["additionalProperties"] == False
    assert definitions["slurm"]["required"] == ["launcher"]

    slurm_properties = definitions["slurm"]["properties"]

    assert slurm_properties["description"]["type"] == "string"
    assert slurm_properties["launcher"]["type"] == "string"
    assert slurm_properties["launcher"]["enum"] == ["sbatch"]

    assert slurm_properties["options"]["type"] == "array"
    assert slurm_properties["options"]["items"]["type"] == "string"
    assert (
        slurm_properties["environment"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert (
        slurm_properties["variables"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert slurm_properties["modules"]["$ref"] == "#/definitions/modules"
    assert slurm_properties["pollinterval"]["type"] == "integer"
    assert slurm_properties["pollinterval"]["minimum"] == 10
    assert slurm_properties["pollinterval"]["maximum"] == 300

    # ------------------ check 'ssh' object ----------------------

    assert "ssh" in definitions
    assert definitions["ssh"]["type"] == "object"
    assert definitions["ssh"]["additionalProperties"] == False
    assert definitions["ssh"]["required"] == ["host", "user", "identity_file"]
    # all keys are string types
    for key in ["description", "host", "user", "identity_file"]:
        assert definitions["ssh"]["properties"][key]["type"] == "string"

    assert (
        definitions["ssh"]["properties"]["environment"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert (
        definitions["ssh"]["properties"]["variables"]["$ref"]
        == "https://buildtesters.github.io/schemas/global/global.schema.json#/definitions/env"
    )
    assert (
        definitions["ssh"]["properties"]["modules"]["$ref"] == "#/definitions/modules"
    )


def test_settings_schema():

    settings_schema = os.path.join(root, "settings", "settings.schema.json")
    # check if file exists
    assert settings_schema

    # load schema and ensure type is a dict
    recipe = load_schema(settings_schema)
    assert isinstance(recipe, dict)

    check_fields(recipe)
    check_properties(recipe["properties"])
    check_definitions(recipe["definitions"])


def test_settings_examples():
    settings_schema = os.path.join(root, "settings", "settings.schema.json")
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
