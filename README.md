# Buildtest Schema

The currently under development types of schemas include:

 - [singlesource](singlesource): a single executable to be run as a test
 - [singlecompile](singlecompile): a compiled build test


## What is a schema?

A schema is the structure of a testing configuration (yaml) file that can
be used to drive one or more tests. For example, if we want to run
a simple bash command, this would use a different schema than a test configuration
that uses a compiler.

## How are schemas defined in buildtest?

Buildtest (will) have a folder of (this type of ) file that define
the structure for each schema. Since each schema type has different versions,
we store those as well:

```bash
buildtest/tools/buildsystem/schemas
   singlesource
   singlecompile
```

## How is this repository organized?

The entire root of this folder could be added to the folder shown above,
and the subfolder structure would be added to the module. Importantly,
the lowercase class names should match to a class defined in in [buildtest/tools/buildsystem/bases.py]().
For example, the contents of the [singlesource](singlesource) directory here are expected 
to be added present at `buildtest/tools/buildsystem/schemas/singlesource` to go
along with a class "SingleSource" in the bases file. This is
the default for a buildsystem model, and it can be changed, however
this is not recommended.


## What are shared attributes?

Every build configuration across types can share some high level metadata,
including a type, description, and maintainer. Additionally, each attribute
should have a key with a unique name so that more than one configuration
can be represented in one file. Here is a quick example for a [singlecompile](singlecompile)
example:


```yaml
# module load example with one version
hello_ex1:
  type: singlesource
  description: "C hello world example1"
  compiler: gnu
  source: hello.c
  scheduler: local
  moduleload:
    key:
      name: GCC
      version: ["6.4.0"]
  cflags:
    - "-O1"
```

The details and required states of all fields are described more clearly
in the [buildtest documentation](https://buildtest.readthedocs.io/en/latest/build_subcommand/singlesource_schema.html) and subfolders here.
**under development!** nothing is finalized or decided yet here.
