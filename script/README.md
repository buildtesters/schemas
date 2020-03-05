# Script

This is the script specification folder for buildtest test configurations.
Notes about sections of the schema are included here. The guide [here](https://cswr.github.io/JsonSchema/)
is a good reference for learning about the schemas.

## Version 0.0.1

This is currently under development.
This line will work share the configuration, as the file will be deployed on GitHub pages.

```
"$id": "https://HPC-buildtest.github.io/schemas/script/script-v0.0.1.schema.json",
```

See how [multiple types](https://cswr.github.io/JsonSchema/spec/multiple_types/) are handled.
Basically, this snippet says that for shell the user can provide a string or an array (a list
of strings or commands to execute). The variables `items`, and `minItems` apply only
in the case that an array is used, and `minLength` applies to commands.

```json
    "shell": {
      "type": ["string", "array"],
      "minLength": 2,
      "minItems": 1,
      "description": "One or more commands to execute to the shell.",
      "items": {
        "type": "string"
      },
    },
```

I believe this says that we require one of "run" or "shell."

```
   "oneOf": [
      { "$ref": "#/definitions/shell" }, 
      { "$ref": "#/definitions/run" } 
    ]
```

I don't currently see a way to represent these definitions external to each file -
it would require serving on a host (web) and then the validator requesting to get
it, which doesn't scale great. So we are choosing redundancy in favor of efficiency.
