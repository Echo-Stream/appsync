# appsync

The EchoStream API.

The API can be found in `schema.graphql`. Other graphql files in this project are
only used for building the documentation.

Generated documentation for this API may be found at https://docs.api.echo.stream.

## Naming conventions
- Objects, Interfaces, Inputs and Unions declarations are `UpperCamelCase`
- Fields are:
  - `UpperCamelCase` if that field acts as a method on the Object
  - `lowerCamelCase` if that field is an attribute of the Object
- Parameters are `lowerCamelCase`

## Queries
All queries are limited to top-level resources in EchoStream. Queries for `Nodes`, `Apps` and `Functions` may return more than one sub-type based on the query parameters.

## Mutations
Direct mutations are limited to creation of resources in EchoStream. 

Further supported mutations are methods (i.e. - `UpperCamelCase` fields) within the type
definitions themselves. Calling these requires a nested GraphQL query that begins with one
of the top-level Query fields.

For example, to delete and drain an `Edge` you could exceute the following GraphQL query:
```graphql
query deleteEdge($source: String!, $target: String!, $tenant: String!) {
  GetEdge(source: $source, target: $target, tenant: $tenant) {
    Delete(drain: true)
  }
}
```
