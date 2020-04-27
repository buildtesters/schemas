import json
import os
import re
import yaml
from jsonschema import validate

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
repo_prefix = "https://buildtesters.github.io/schemas"


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


def test_schema_naming(tmp_path):
    """ensure that schemas are named accordingly including:
       - no special characters in folders/names in the root directory
       - files in subfolders follow schema-v[version].[name].json
       - semver is used for version
       - examples folder has subfolders that correspond to existing versions
       - each example has a version that corresponds with it's folder
    """
    skips = ["README.md", "global", "LICENSE", "examples", "settings"]
    print("Root of testing is %s" % root)

    # Read in the outer validator (looks for list with keys and version)
    outer_file = os.path.join(root, "global", "global.schema.json")
    assert os.path.exists(outer_file)
    outer_schema = load_schema(outer_file)

    for schema_name in os.listdir(root):

        if (
            schema_name in skips
            or re.search("^([.]|_)", schema_name)
            or os.path.isfile(schema_name)
        ):
            continue

        schema_dir = os.path.abspath(schema_name)
        print("Testing schema %s" % schema_name)

        # No special characters in schema name
        assert re.search("^[a-zA-Z]+$", schema_name)

        schemas = os.listdir(schema_dir)
        for schema in schemas:

            if schema in skips:
                continue

            # Assert it loads with jsonschema
            schema_file = os.path.join(schema_dir, schema)
            loaded = load_schema(schema_file)

            # Ensure that other requireds are included and properly formatted
            fields = ["$id", "$schema", "title", "propertyNames", "properties"]
            for field in fields:
                assert field in loaded

            # Check individual schema properties
            assert loaded["$id"] == "%s/%s/%s" % (repo_prefix, schema_name, schema)
            assert loaded["$schema"] == "http://json-schema.org/draft-07/schema#"
            assert loaded["type"] == "object"
            assert loaded["propertyNames"] == {"pattern": "^[A-Za-z_][A-Za-z0-9_]*$"}

            # Assert is named correctly
            print("Checking naming of %s" % schema)
            match = re.search(
                "%s-v(?P<version>[0-9]{1}[.][0-9]{1}[.][0-9]{1})[.]schema[.]json"
                % schema_name,
                schema,
            )
            assert match

            # Ensure we found a version
            assert match.groups()
            version = match["version"]

            assert "required" in loaded
            # check "type" and "run" are required keys
            assert "type" in loaded["required"]
            assert "run" in loaded["required"]

            # check all keys are properties
            found = [
                "type",
                "description",
                "maintainers",
                "env",
                "executor",
                "shell",
                "pre_run",
                "run",
                "post_run",
                "status",
            ]
            print(f"Checking all keys: {found} in schema 'properties'")
            loaded_properties = list(loaded["properties"].keys())
            for prop in found:
                print("Checking for property %s in %s" % (prop, schema_file))
                assert prop in loaded_properties

            # 'type' key takes a pattern string that must start and end with the word 'script'
            assert loaded["properties"]["type"]["pattern"] == "^script$"

            # check all properties that are string types
            for section in [
                "type",
                "description",
                "pre_run",
                "post_run",
                "shell",
                "shebang",
                "executor",
            ]:
                assert loaded["properties"][section]["type"] == "string"

            # check all properties that are object types
            assert loaded["properties"]["env"]["type"] == "object"
            assert loaded["properties"]["status"]["type"] == "object"

            # check all properties that are array types
            assert loaded["properties"]["maintainers"]["type"] == "array"

            assert "pattern" in loaded["properties"]["shell"]
            assert (
                loaded["properties"]["shell"]["pattern"]
                == "^(/bin/bash|/bin/sh|sh|bash|python).*"
            )

            # check status object
            status_properties = loaded["properties"]["status"]["properties"]
            assert "returncode" in status_properties
            assert "regex" in status_properties
            # regex has required fields for stream and exp, both must be defined
            assert "required" in status_properties["regex"]
            # check type for returncode and regex key
            assert status_properties["returncode"]["type"] == "integer"
            assert status_properties["regex"]["type"] == "object"

            status_regex_properties = loaded["properties"]["status"]["properties"][
                "regex"
            ]["properties"]
            # check for key 'stream' and 'exp' in regex object
            assert "stream" in status_regex_properties
            assert "exp" in status_regex_properties
            # check type for 'stream' and 'exp' key in regex object
            assert status_regex_properties["stream"]["type"] == "string"
            assert status_regex_properties["exp"]["type"] == "string"

            # Ensure a version folder exists with at least one recipe
            print("Checking examples for %s" % schema)
            examples = os.path.join(schema_dir, "examples", version)

            assert os.path.exists(examples)

            recipes = os.listdir(examples)
            assert recipes
            for recipe in recipes:
                assert recipe

                assert re.search("(yml|yaml)$", recipe)
                recipe_path = os.path.join(examples, recipe)
                content = load_recipe(recipe_path)

                # Validate outer structure (and version included)
                validate(instance=content, schema=outer_schema)

                # Ensure version is correct in header
                assert content["version"] == version
                del content["version"]

                # For each section, assume folder type and validate
                for name, section in content.items():
                    print("Testing %s from recipe %s" % (name, recipe))
                    validate(instance=section, schema=loaded)
