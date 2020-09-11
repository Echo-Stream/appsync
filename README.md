pk:
  Users: username
  All others: tenant name

sk:
  Users: T~<tenant>
  Tenant: T~
  Edge: E~<source|target> 

User:
pk: <email>
sk: T~<tenant>
role: string
invitation_token: string
invitation_accepted_date: string

Tenant:
sk: tenant ame

