# HL7-Ninja Appsync API

## Indexes
#### Primary Key (composit):
* pk (partition)
* sk (sort)

#### lsi0 (composit):
* lsi0_sk (sort)
* projection: ALL_ATTRIBUTES

#### gsi0 (partition only):
* gsi0_pk
* projection: gsi0_pk, pk and status

## Schema
