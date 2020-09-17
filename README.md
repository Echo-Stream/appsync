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

#### App

|<item type>| pk      |sk                  |lsi0_sk               |tenant  |name  |type       |metadata|source       |target       |app_id|auth_type   |account              |email    |gsi0_pk |iso          |default_region|billing_info|event_id|
|-----------|---------|--------------------|----------------------|--------|------|-----------|--------|-------------|-------------|------|------------|---------------------|---------|--------|-------------|--------------|------------|--------|
|Tenant     |<name>   |T~                  |                      |        |<name>|           |{}      |             |             |<uuid>|            |                     |         |        |             |<aws region>  |{}          |<uuid>  |
|User       |<tenant> |U~<email>           |                      |<tenant>|<name>|           |{}      |             |             |      |            |                     |<email>  |<email> |             |              |            |        |
|App        |<tenant> |A~<name>            |                      |<tenant>|<name>|$app_type  |{}      |             |             |      |$auth_type  |<aws account number> |         |        |<b64 string> |              |            |        |
|Node       |<tenant> |N~<name>            |                      |<tenant>|<name>|$node_type |{}      |<source node>|<target node>|      |            |                     |         |        |             |              |            |        |
|Edge       |<tenant> |E~<source>\|<target>|E~<target>\|<source>  |<tenant>|<name>|           |{}      |             |             |      |            |                     |         |        |             |              |            |        |

* $app_type = Hl7App | EdgeApp
* $node_type = Hl7InboundNode | Hl7OutboundNode | ExternalNode | CustomNode
* $auth_type = cognito | x_account

### Immutable attributes
Changes to these attributes cause a "Condition check failed" exception for existing items. Once an item is created the arguments for these attributes must match the original
* account
* auth_type
* type
* tenant
* email
* name
* gsi0_pk
* sk (Tenants, Users, App, Node)
