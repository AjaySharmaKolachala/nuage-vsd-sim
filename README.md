# vspk-sim
A sample Nuage VSD API simulator

## Supported Features
* Supported entities:
  * Enterprise
  * User
  
* Basic CRUD operations on root level of objects
  * `.get()`
  * `.get_first()` - See limitations
  * `.fetch()`
  * `.delete()`
  * `.save()`
  * `.create_child()` - See limitations 

## Limitations
* Request headers are not yet parsed, as such pagination and fetching a single entity do not work. (`get_first` works through Bambou)
* Creating a child does not link it to its parent yet, only useful for root objects at this point.
  