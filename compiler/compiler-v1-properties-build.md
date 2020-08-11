# Untitled object in BuildTest Schema for compiler Schema

```txt
https://buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [compiler-v1.0.schema.json\*](../../out/compiler-v1.0.schema.json "open original schema") |

## build Type

`object` ([Details](compiler-v1-properties-build.md))

# undefined Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :-------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-name.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/name")         |
| [cc](#cc)             | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cc.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cc")             |
| [fc](#fc)             | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-fc.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/fc")             |
| [cxx](#cxx)           | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cxx.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cxx")           |
| [source](#source)     | `string` | Required | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-source.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/source")     |
| [cflags](#cflags)     | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cflags")     |
| [cxxflags](#cxxflags) | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cxxflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cxxflags") |
| [fflags](#fflags)     | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-fflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/fflags")     |
| [cppflags](#cppflags) | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cppflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cppflags") |
| [ldflags](#ldflags)   | `string` | Optional | cannot be null | [BuildTest Schema for compiler](compiler-v1-properties-build-properties-ldflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/ldflags")   |

## name




`name`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-name.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/name")

### name Type

`string`

### name Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | ----------- |
| `"gnu"`   |             |
| `"intel"` |             |
| `"pgi"`   |             |
| `"cray"`  |             |

## cc




`cc`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cc.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cc")

### cc Type

`string`

## fc




`fc`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-fc.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/fc")

### fc Type

`string`

## cxx




`cxx`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cxx.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cxx")

### cxx Type

`string`

## source




`source`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-source.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/source")

### source Type

`string`

## cflags




`cflags`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cflags")

### cflags Type

`string`

## cxxflags




`cxxflags`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cxxflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cxxflags")

### cxxflags Type

`string`

## fflags




`fflags`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-fflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/fflags")

### fflags Type

`string`

## cppflags




`cppflags`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-cppflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/cppflags")

### cppflags Type

`string`

## ldflags




`ldflags`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [BuildTest Schema for compiler](compiler-v1-properties-build-properties-ldflags.md "https&#x3A;//buildtesters.github.io/schemas/compiler/compiler-v1.0.schema.json#/properties/build/properties/ldflags")

### ldflags Type

`string`
