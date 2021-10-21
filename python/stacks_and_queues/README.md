# Stacks and Queues
- `Stack` is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.
- `Queue` is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge
- Bild data structures with stacks and queues and implement methods on them like `push`, `pop`, `peek` and `is_empty` on `Stacks`, also, `enqueue`, `dequeue`, `peek`, and `is_empty`on `Queues`

## Approach & Efficiency
- Buliding a node, stack and quesues classes and implement the methods mention above on them
- The big O notiation for space and stime for both queues and stacks is O(1)

## API
- Stacks
    - `push`:
    ```
    Description: This function pushs nodes into the stack when called

    Args:
        value (int or str)
    ```
    - `pop`:
    ```
    Description: This function remove a node from the stack when called
    return: the value of the removed node
    ```
    - `peek`:
    ```
    Description: This function shows the top node in the stack when called
    return: the value of the top node
    ```
    - `is_empty`:
    ```
    Description: This function checks if the stack is empty
    return: True, if the stack is empty
            False, if the stack is not empty
    ```
- Queues
    - `enqueue`:
    ```
    Description: This function pushs nodes into the end of the queue when called

    Args:
        value (int or str)
    ```
    - `dequeue`:
    ```
    Description: This function remove a node from the front of the queue when called
    ```
    - `peek`:
    ```
    Description: This function shows the front node in the queue when called
    return: the value of the top node
    ```
    - `is_empty`:
    ```
    Description: This function checks if the queue is empty
    return: True, if the queue is empty
            False, if the queue is not empty
    ```


