# Compiler 

The compiler schema is used by buildtest to compile source files into an 
executable. The schema supports open-source compilers like ``gnu``, ``pgi`` and 
proprietary compilers like ``intel`` and ``cray``.  The schema documentation
is based on  [compiler-v1.0.schema.json](https://buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json).


## Compiler Schema Fields

| Name | Type | Supported in Buildtest | Required | Description | Valid Options | 
| ---- | ---- | ---------------------- | ----------- | -------- | -------------- |
| type | string | YES | YES | The schema type to validate test | `compiler` | 
| description | string | YES | NO |  A brief description of the test | 
| vars | object | YES | NO |  inherited |
| env | object | YES | NO | inherited | 
| module | array | YES | NO | A list of modules to inject into test | 
| compiler | object | YES | YES | Define compiler setting to compile a script |  
| sbatch | object | YES | NO | inherited | 
| status | object | YES | NO | inherited | 


## compiler object

| Name | Type | Supported in Buildtest | Required | Description | Valid Options |   
| ---- | ---- | --------------------- | ------------ | ------------ | ---------- |  
| name | string | YES | YES | Select a compiler name, based on selection buildtest will detect the appropriate compiler wrapper. | `gnu`, `intel`, `pgi`, `cray` | 
| source | string | YES | YES | Select a source file to compile, the file could be an absolute path or relative path from Buildspec | 
| cc | string | YES | NO | Set C compiler wrapper. Use this option to manually set compiler wrapper |
| cxx | string | YES | NO | Set C++ compiler wrapper. Use this option to manually set compiler wrapper |
| fc | string | YES | NO | Set Fortran compiler wrapper. Use this option to manually set compiler wrapper |
| exec_args | string | YES | NO | Pass arguments to compiled executable | 
| cflags | string | YES | NO | Specify C compiler options |  
| cxxflags | string | YES | NO | Specify C++ compiler options |  
| fflags | string | YES | NO | Specify Fortran compiler options | 
| cppflags | string | YES | NO | Specify pre-processor options | 
| ldflags | string | YES| NO | Specify linker options for dynamic linking | 





 