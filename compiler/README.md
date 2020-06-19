# Compiler 

The compiler schema is used by buildtest to compile source files into an 
executable. The schema supports multiple compilers, while only one can be 
selected at a time using the `name` key. This schema is in development 
and subject to change.

The compiler schema is available at https://buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json

## State: In Development

## Main Keys

| Name | Type | Supported in Buildtest | Description | 
| ---- | ---- | ---------------------- | ----------- |
| type | string | YES | The schema type must be `compiler` | 
| description | string | YES | A brief description of the test | 
| module | array | YES | A list of modules to inject into test | 
| compiler | object | YES | Define compiler setting to compile a script |  

Required Keys: [`type`,`compiler`, `executor`]


# Keys inherited from global.schema.json

- env
- status
- executor
- sbatch

## Compiler Key

| Name | Type | Supported in Buildtest | Description  |   
| ---- | ---- | --------------------- | ------------ |  
| name | string | YES | Select a compiler name, based on selection buildtest will detect the appropriate compiler wrapper. Valid options are `gnu`, `intel`, `pgi`, `cray` | 
| source | string | YES | Select a source file to compile, the file could be an absolute path or relative path from Buildspec | 
| exec_args | string | YES | Pass arguments to compiled executable | 
| cflags | string | YES | Specify C compiler options |  
| cxxflags | string | YES | Specify C++ compiler options |  
| fflags | string | YES | Specify Fortran compiler options | 
| cppflags | string | YES | Specify pre-processor options | 
| ldflags | string | YES| Specify linker options for dynamic linking | 

Required Keys: [`name`,`source`]



 