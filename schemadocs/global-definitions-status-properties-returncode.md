# Untitled integer in buildtest global schema Schema

```txt
https://buildtesters.github.io/schemas/schemas/global.schema.json#/definitions/status/properties/returncode
```

By default, returncode 0 is PASS, if you want to emulate a non-zero returncode to pass then specify an expected return code. buildtest will match actual returncode with one defined in this field, if there is a match buildtest will report as `PASS`


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [global.schema.json\*](../out/global.schema.json "open original schema") |

## returncode Type

`integer`
