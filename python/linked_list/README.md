# Singly Linked List
This challenge repreasent a singliy linked list with its basics and how to create the nodes and implement them with different methods

## Challenge
Implementing methods on data structures and creating the nodes

## Approach & Efficiency
This challenge enhanced my logic understanding of the linked list
- `Insert` method has O(1) big O complexity for time and space
- `Includes` method has O(n) big O complexity for time and space
- `to_string` method has O(n) big O complexity for time and space

## API
- `instert`
```
        """
Insert creates a Node with the value that was passed and adds
it to the head of the linked list shifting all other values down

Arguments:
value : any

Returns: None
```
- `Includes`

```
Includes Indicates whether that value exists as a Node’s value somewhere within the list.

Arguments: Value

Returns: Boolean

```
- `to_string`
```
Includes Indicates whether that value exists as a Node’s value somewhere within the list.

Arguments: none

Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
```

- `insert_after`

```
Insert_after is a method adds a new node with the given new value immediately after the first node that has the value specified

Arguments: value, new value

Returns: a list with added node after the value specified
```


- `insert_before`
```
Insert_before is a method adds a new node with the given new value immediately before the first node that has the value specified

Arguments: value, new value

Returns: a list with added node before the value specified
```

- `append`
```

Append function adds a node to the end of the list

Arguments: new value

Returns: list with a new node in its ending

```


# Check List
- [x] Can successfully instantiate an empty linked list

- [x] Can properly insert into the linked list

- [x] The head property will properly point to the first node in the linked list

- [x] Can properly insert multiple nodes into the linked list

- [x] Will return true when finding a value within the linked list that exists

- [x] Will return false when searching for a value in the linked list that does not exist
