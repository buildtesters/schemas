# Buildtest Schema

The currently (under development) types of schemas include:

 - [script](script): a single executable or multiple lines to be run as a test
 - [global](global): includes a simple global schema that is not expected to change frequently. This mandates that every recipe is a yaml file with a version and one or more named subsections.

## What is a schema?

A schema is the structure of a testing configuration (yaml) file that can
be used to drive one or more tests. The schemas themselves are represented in
json, and this is because we use [jsonschema](https://json-schema.org/learn/miscellaneous-examples.html)
and yaml is read in to Python as json as well. Each schema corresponds to a specific
kind of test, and the names should be somewhat intuitive. For example, if we want to run
a simple bash command, this would use a different schema than a test configuration
that uses a compiler.

## How are schemas defined in buildtest?

Buildtest (will) have a folder of (this type of ) file that define
the structure for each schema. Since each schema type has different versions,
we store those as well:

```bash
buildtest/buildsystem/schemas
   script
```

The above would include a folder of schemas for the "script" type, each named by a version.
For example:


```bash
script/
    script-v0.0.1.schema.json
    script-v0.0.2.schema.json
    ...
```


## How is this repository organized?

The entire root of this folder could be added to the folder shown above,
and the subfolder structure would be added to the module. Importantly,
the lowercase class names should match to a class defined in [buildtest/tools/buildsystem/bases.py]().
For example, the contents of the [script](script) directory here are expected 
to be added present at `buildtest/tools/buildsystem/schemas/script` to go
along with a class "Script" in the bases file. 

## What are optional shared attributes?

### Metadata 

Every build configuration across types can share some high level metadata,
including a type, description, and maintainers. Additionally, each attribute
should have a key with a unique name so that more than one configuration
can be represented in one file. The fields are summarized below:

| Name | Description | Type | Required for Schema | Required for User |
| ---- | ----------- | ---- | ------------------- | ----------------- |
| type | the name of the schema type (e.g., "script") | string | true | true |
| description | a description of the build | string | true | false |
| maintainers | a list of one or more maintainers | array | true | false |

Here is a quick example for a [script](script) example:


```yaml
version: 0.0.1
hello_ex1:
  type: script
  description: "hello world example"
  maintainers: 
   - "@vsoch"
  shell: "echo hello"
```

Note that the outer structure (the version and general yaml file with named sections)
is tested by the [global](global) schema. The contents of the section `hello_ex1`
are of type script, and thus are tested by the [script](script) schema.
The above would say to use version 0.0.1 of the script schema to run the test.
The parameters for the description, and maintainers are optional but shown here.
Each recipe is tested that these required fields are included (but optional).


### Build Steps

By default, each test configuration schema should have the following optional fields:

| Name | Description | Type | Required for Schema | Required for User | Default |
| ---- | ----------- | ---- | ------------------- | ----------------- | -------- |
| pre_run | script to run before build | string | true | false | |
| post_run | script to run after build | string | true | false | |
| shell | shell interpreter to use for pre and post run | string | true | false | bash |
| env | an object (dict) of custom environment variables | object with objects | true | false |  |

The build command generated based on the configuration type, is sandwiched between
the pre and post run sections:

 - pre_run
 - run
 - post_run

And shell must also be defined (defaulting to usually bash, but this may vary) to
know the shell to use if these statements are defined. Of course more complex 
classes that might require additional sections (e.g., pre and
post compile) can still define these as valid sections for their config recipes,
and they are handled by a custom class. The only important point
for now is that `pre_run` and `post_run` are required (and tested for) for
a general schema (optional for the user).

## How to contribute

### Adding a new schema

Each schema in buildtest for a test configuration is represented here.
If you want to make a new schema to add to buildtest:

 1. add a new folder that corresponds to the name of the schema. It should be all letters (uppercase and lowercase) with no special characters.
 2. the folder can optionally have a README.md where you keep notes about the specification design.
 3. the folder should have a subfolder called "examples" and a subfolder for each version of the recipe
 4. ensure that the name of the schema is in the format (e.g., `script-v0.0.1.schema.json`)
 5. for content, you can start with another schema (from a different folder) as an example. 
 6. you should add one or more valid examples to each version folder under examples (e.g., `script/examples/0.0.1/example.yml`). These examples will be tested against your schema for validity.
 6. you should add one or more invalid examples under `.github/tests/invalid/<name>/<version>/` (e.g., `.github/tests/invalid/script/0.0.1/invalid-reason.yml`).

Be sure to update properties and take account for:
  - a property being required or not
  - requirements for the values provided (types, lengths, etc.) 
  - If you need help, see [resources](#resources) or [ask a question](https://github.com/HPC-buildtest/schemas/issues)

### Adding a new version

Adding a new version means that you only need to:

 - create a new file with the version (e.g. `script-v0.0.2.schema.json`)
 - add a folder for the version under examples for the parent folder
 - add one or more invalid examples to be tested under `.github/tests/invalid/<name>/<version>`

In both cases, when the version is finished, a release means adding the file to
buildtest under `buildtest/tools/buildsystem/schemas`

## Development Tips

**Note that these are examples, and not necessarily implemented sections for test config types**

### Multiple Types

See how [multiple types](https://cswr.github.io/JsonSchema/spec/multiple_types/) are handled.
Basically, this snippet says that for shell the user can provide a string or an array (a list
of strings or commands to execute). The variables `items`, and `minItems` apply only
in the case that an array is used, and `minLength` applies to commands.

```json
    "shell": {
      "type": ["string", "array"],
      "minLength": 2,
      "minItems": 1,
      "description": "One or more commands to execute to the shell.",
      "items": {
        "type": "string"
      },
    },
```

I believe this says that we require one of "run" or "shell."

```
   "oneOf": [
      { "$ref": "#/definitions/shell" }, 
      { "$ref": "#/definitions/run" } 
    ]
```


## Resources

The following sites (along with the files here) can be useful to help with your development
of a schema.

 - [json-schema.org](https://json-schema.org/understanding-json-schema/)
 - [json schema readthedocs](https://python-jsonschema.readthedocs.io/en/stable/)
