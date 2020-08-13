# Untitled object in buildtest configuration schema Schema

```txt
https://buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## ssh Type

`object` ([Details](settings-definitions-ssh.md))

# undefined Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------------------ | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description)     | `string` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-ssh-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/description")     |
| [host](#host)                   | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-ssh-properties-host.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/host")                   |
| [user](#user)                   | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-ssh-properties-user.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/user")                   |
| [identity_file](#identity_file) | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-ssh-properties-identity_file.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/identity_file") |
| [environment](#environment)     | `object` | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/environment")                              |
| [variables](#variables)         | `object` | Optional | cannot be null | [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/variables")                                |
| [modules](#modules)             | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/modules")                            |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-ssh-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/description")

### description Type

`string`

## host




`host`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-ssh-properties-host.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/host")

### host Type

`string`

## user




`user`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-ssh-properties-user.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/user")

### user Type

`string`

## identity_file




`identity_file`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-ssh-properties-identity_file.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/identity_file")

### identity_file Type

`string`

## environment

One or more key value pairs for an environment (key=value)


`environment`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/environment")

### environment Type

`object` ([Details](global-definitions-env.md))

### environment Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## variables

One or more key value pairs for an environment (key=value)


`variables`

-   is optional
-   Type: `object` ([Details](global-definitions-env.md))
-   cannot be null
-   defined in: [buildtest configuration schema](global-definitions-env.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/variables")

### variables Type

`object` ([Details](global-definitions-env.md))

### variables Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [buildtest configuration schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/schemas/settings.schema.json#/definitions/ssh/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
