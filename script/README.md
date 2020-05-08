# Script

This is the script specification folder for buildtest test configurations.
Notes about sections of the schema are included here. The guide [here](https://cswr.github.io/JsonSchema/)
is a good reference for learning about the schemas.

## Version 0.0.1

This is currently under development.
This line will work share the configuration, as the file will be deployed on GitHub pages.

```
"$id": "https://buildtesters.github.io/schemas/script/script-v0.0.1.schema.json",
```

The fields `$id`, `$schema`, `$title`,  `$type` `required`, `propertyNames`,
and `properties` are required (and tested for) higher level schema attributes.
In the table below, we show properties defined under "properties". The
table below is represented in the schema file.


| Name | Description | Type | Required for Schema | Required for User | Default |
| ---- | ----------- | ---- | ------------------- | ----------------- | -------- |
| type | the type (must be script) | string | true | true | |
| description | a description of the build | string | true | false | |
| env | an object (dict) of custom environment variables | object with objects | true | false |  |
| shell | shell interpreter to use for run section | string | true | false | bash |
| run | main script to run | string | true | true | |
| executor | name of executor to dispatch job defined in buildtest configuration | string | true | false | |
