# Buildtest Wrapper Schema

This schema is designed to run across build test recipes, regardless of
the underlying configuration test types that are represented. The general
idea is that a testing file consists of a version plus one or more tests
to run, each of which can correspond to a different type.

Currently, a recipe file must include a version, and we do this
so that build test is very explicit about how the configuration files
are pased.  If tests in one file
require different versions, this will currently require creating
a new file. It could be an option to add a version variable to a section
to override the global version, however this is not yet implemented.


