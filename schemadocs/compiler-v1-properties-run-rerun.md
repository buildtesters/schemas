# Untitled integer in compiler schema version 1.0 Schema

```txt
https://buildtesters.github.io/schemas/schemas/compiler-v1.0.schema.json#/properties/run/rerun
```

Number of times to rerun test. By default every test is run once. Rerun expects a value >= 1


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                             |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [compiler-v1.0.schema.json\*](../out/compiler-v1.0.schema.json "open original schema") |

## rerun Type

`integer`

## rerun Constraints

**minimum**: the value of this number must greater than or equal to: `1`
