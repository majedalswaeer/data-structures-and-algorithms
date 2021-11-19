# Hash Tables

## Description
- This challenge representing the new data structure that we took which is the hash table

## Challenge
- Implementing a hash table that is able to add key/value pairs to it

## Approach & Efficiency
- All methods existed in the hash table is not exceeding big O(n), that the benefit of the hash table that we can retrieve, add and check our data in a very low time and space complexity.

## API

- `Hash`

    ```
    Hash function which hash the given key with specfic number

            Args:
                key ([type]): Any

            Returns:
                Integer
    ```
- `Add`

    ```
    Add function adds a key/value pair into the hash table

            Args:
                key ([type]): Any
                value ([type]): Any
    ```
- `Get`

    ```
    Get function retrive a value that is associated with the given key

            Args:
                key ([type]): Any

            Returns:
                Value if existed (Any type of data)
                Exception if the key does not exist

    ```
- `Contains`

    ```
    Contain function checks whether if the key given existed or not in the hash table

            Args:
                key ([type]): Any

            Returns:
                [type]: Boolean

    ```
