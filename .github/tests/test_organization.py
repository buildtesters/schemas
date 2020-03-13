#!/usr/bin/python

# Copyright (C) 2020 Vanessa Sochat.

# This Source Code Form is subject to the terms of the MIT License.
# If a copy of the MIT license was not distributed with this file,
# you can obtain one at https://choosealicense.com/licenses/mit/.

from jsonschema import validate

import json
import os
import re
import shutil
import pytest
import yaml

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
repo_prefix = "https://HPC-buildtest.github.io/schemas"


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
    skips = ["README.md", "global", "LICENSE", "examples"]
    print("Root of testing is %s" % root)

    # Read in the outer validator (looks for list with keys and version)
    outer_file = os.path.join(root, "global", "outer.schema.json")
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

            # Type is always required
            assert "required" in loaded
            assert "type" in loaded["required"]
            assert "type" in loaded["properties"]

            # pre_run, post_run, and shell are required for all schemas
            for section in ["pre_run", "post_run", "shell"]:
                assert section in loaded["properties"]
                assert loaded["properties"][section]["type"] == "string"

            # Assert that description, maintainers, and version are in properties
            properties = ["description", "maintainers"]
            print("Checking for optional properties %s" % properties)
            found = list(loaded["properties"].keys())
            for prop in properties:
                print("Checking for property %s in %s" % (prop, schema_file))
                assert prop in found
                assert prop not in loaded["required"]

            # Check individual schema properties
            assert loaded["$id"] == "%s/%s/%s" % (repo_prefix, schema_name, schema)
            assert loaded["$schema"] == "http://json-schema.org/draft-07/schema#"
            assert loaded["type"] == "object"
            assert loaded["propertyNames"] == {"pattern": "^[A-Za-z_][A-Za-z0-9_]*$"}

            # Assert is named corretly
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
