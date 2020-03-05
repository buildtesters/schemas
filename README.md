# Buildtest Schema

The currently under development types of schemas include:

 - [script](script): a single executable or multiple lines to be run as a test

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
buildtest/tools/buildsystem/schemas
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

## What are shared attributes?

Every build configuration across types can share some high level metadata,
including a type, description, and maintainer. Additionally, each attribute
should have a key with a unique name so that more than one configuration
can be represented in one file. Here is a quick example for a [script](script)
example:


```yaml
version: 0.0.1
hello_ex1:
  type: script
  description: "hello world example"
  maintainer: "@vsoch"
  shell: "echo hello"
```

The above would say to use version 0.0.1 of the script schema to run the test.
The parameters for the description, and maintainer are optional but shown here.

**under development!** nothing is finalized or decided yet here.
