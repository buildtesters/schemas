#!/usr/bin/python

# Copyright (C) 2020 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from jsonschema import validate

import json
import os
import re
import shutil
import pytest
import yaml

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    skips = ["README.md", "global"]
    print("Root of testing is %s" % root)

    # Read in the outer validator (looks for list with keys and version)
    outer_file = os.path.join(root, "global", "outer.schema.json")
    assert os.path.exists(outer_file)
    outer_schema = load_schema(outer_file)

    for schema_name in os.listdir(root):
        if schema_name in skips or re.search("^([.]|_)", schema_name):
            continue

        schema_dir = os.path.abspath(schema_name)
        print("Testing schema %s" % schema_name)

        # No special characters in schema name
        assert re.search("^[a-zA-Z]+$", schema_name)

        schemas = os.listdir(schema_dir)
        for schema in schemas:

            if schema in ["README.md", "examples"]:
                continue

            # Assert it loads with jsonschema
            schema_file = os.path.join(schema_dir, schema)
            loaded = load_schema(schema_file)

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
