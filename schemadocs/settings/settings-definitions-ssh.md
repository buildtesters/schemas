# Untitled object in Buildtest Settings Schema Schema

```txt
https://buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../../out/settings.schema.json "open original schema") |

## ssh Type

`object` ([Details](settings-definitions-ssh.md))

# undefined Properties

| Property                        | Type          | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :------------------------------ | ------------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description)     | `string`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/description")     |
| [host](#host)                   | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-host.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/host")                   |
| [user](#user)                   | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-user.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/user")                   |
| [identity_file](#identity_file) | `string`      | Required | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-identity_file.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/identity_file") |
| [environment](#environment)     | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/environment")     |
| [variables](#variables)         | Not specified | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-ssh-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/variables")         |
| [modules](#modules)             | `object`      | Optional | cannot be null | [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/modules")                            |

## description




`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-description.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/description")

### description Type

`string`

## host




`host`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-host.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/host")

### host Type

`string`

## user




`user`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-user.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/user")

### user Type

`string`

## identity_file




`identity_file`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-identity_file.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/identity_file")

### identity_file Type

`string`

## environment




`environment`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-environment.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/environment")

### environment Type

unknown

## variables




`variables`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-ssh-properties-variables.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/variables")

### variables Type

unknown

## modules




`modules`

-   is optional
-   Type: `object` ([Details](settings-definitions-modules.md))
-   cannot be null
-   defined in: [Buildtest Settings Schema](settings-definitions-modules.md "https&#x3A;//buildtesters.github.io/schemas/settings/settings.schema.json#/definitions/ssh/properties/modules")

### modules Type

`object` ([Details](settings-definitions-modules.md))
