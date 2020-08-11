# Buildtest Schema

This repository contains the schemas used by buildtest. The development of schema
is done independent of the framework. 

buildtest buildspec schemas are the following:

- [global](schemadocs/global): global schema defines values that are global to all schema files and it is validated with all buildspecs.
- [script](schemadocs/script): This schema is for `type: script` in buildspec for writing shell scripts scripts 
- [compiler](schemadocs/compiler): This schema is for `type: compiler` in buildspec for compiling programs with compilers such as GNU, Intel, PGI, etc...
- [python](schemadocs/python): This schema is for `type: python`  in buildspec for writing python scripts.

To configure buildtest use the `settings.schema.json`:
- [settings](schemadocs/settings): This schema defines the content of buildtest settings file to configure buildtest.

## What is a schema?

A schema defines the structure of how to write and validate a JSON file. Since,
python can load YAML and JSON files we write our Buildspecs in YAML and validate
them with a schema file that is in json. 

We make use of [python-jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)
run `validate` with a Buildspec with one of the schema file. 
 
## Resources

The following sites (along with the files here) can be useful to help with your development
of a schema.

 - [json-schema.org](https://json-schema.org/)
 - [json schema readthedocs](https://python-jsonschema.readthedocs.io/en/stable/)
 
If you have issues with writing json schema please join the [JSON-SCHEMA Slack Channel](http://json-schema.slack.com)
 
## How are schemas defined in buildtest?

Buildtest will contain a folder per schema (`script`, `global`, `compiler`, etc...) that 
contains one or more versions of the schema. Since each schema type has 
different versions we store them in format such as :

```
script-v1.0.schema.json
```

The format is `<name>-vX.Y.schema.json`

These schemas are also stored in buildtest [here](https://github.com/buildtesters/buildtest/tree/devel/buildtest/schemas)


## How is this repository organized?

The entire root of this folder could be added to the folder shown above,
and the subfolder structure would be added to the module. Importantly,
the lowercase class names should match to a class defined in [buildtest/buildsystem/bases.py](https://github.com/buildtesters/buildtest/tree/devel/buildtest/buildsystem/base.py).
For example, the contents of the [script](script) directory here are expected 
to be added present at `buildtest/schemas/script` to go
along with a class "Script" in the bases file. 


## How to contribute

### Adding a new schema

Each schema in buildtest for a test configuration is represented here.
If you want to make a new schema to add to buildtest:

 1. add a new folder that corresponds to the name of the schema. It should be all letters (uppercase and lowercase) with no special characters.
 2. the folder can optionally have a README.md where you keep notes about the specification design.
 3. the folder should have a subfolder called "examples" and a subfolder for each version of the recipe
 4. ensure that the name of the schema is in the format (e.g., `script-v1.0.schema.json`)
 5. you should add one or more valid examples to each version folder, for instance script 1.0 valid examples are under examples (e.g., `tests/valid/script/1.0/`). 
 6. you should add one or more invalid examples for example script 1.0 invalid examples are at `tests/invalid/script/1.0`
 7. Finally add regression test to validate schema definition and run a set of valid, invalid tests until all checks are passed and you are comfortable with schema design then issue a PR. 
 
Be sure to update properties and take account for:
  - a property being required or not
  - Make use of `additionalProperties: false` when defining properties so that additional keys in properties are not passed in.
  - requirements for the values provided (types, lengths, etc.) 
  - If you need help, see [resources](#resources) 
    or reach out to someone in Slack.

### Adding a new version

Adding a new version means that you only need to:

 - create a new file with the version (e.g. `script-v2.0.schema.json`)
 - add a folder for the version under examples for the parent folder
 - add one or more invalid examples to be tested under `.github/tests/invalid/<name>/<version>`

In both cases, when the version is finished, a release means adding the file to
buildtest under `buildtest/buildsystem/schemas` and implement the changes
required in buildtest to support the schema. 


