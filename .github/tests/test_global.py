#!/usr/bin/python

# Copyright (C) 2020 Vanessa Sochat.

# This Source Code Form is subject to the terms of the MIT License.
# If a copy of the MIT license was not distributed with this file,
# you can obtain one at https://choosealicense.com/licenses/mit/.

from jsonschema import validate
from jsonschema.exceptions import ValidationError

import json
import os
import re
import pytest
import yaml

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


def test_global_schema(tmp_path):
    """Invalid examples should be under ./invalid/global.
    """
    print("Root of testing is %s" % root)

    # Read in the outer validator (looks for list with keys and version)
    outer_file = os.path.join(root, "global", "outer.schema.json")
    assert os.path.exists(outer_file)
    outer_schema = load_schema(outer_file)

    print("Testing global schema")

    # Missing version
    outer_recipe = os.path.abspath(
        os.path.join(here, "invalid", "global", "missing-version.yml")
    )
    assert os.path.exists(outer_recipe)
    assert re.search("(yml|yaml)$", outer_recipe)
    content = load_recipe(outer_recipe)

    # Version is required
    with pytest.raises(ValidationError) as excinfo:
        validate(instance=content, schema=outer_schema)
        assert "'version' is a required property" in str(excinfo.value)
