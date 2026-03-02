def ft_filter(function, iterable):
    """
    ft_filter(function, iterable) --> list

    Applies function to each item in iterable and returns a list
    containing only the items for which function(item) is true.

    Args:
        function (callable): A function that takes a single argument
                             and returns a boolean value.
        iterable (iterable): Any iterable object (list, tuple, string, etc.)
                             whose items will be evaluated.

    Returns:
        list: A new list containing only the items where function(item)
        is True.

    Example:
        >>> ft_filter(lambda word: len(word) > 4, ["Hello", "the", "World"])
        ['Hello', 'World']
    """

    return [item for item in iterable if function(item)]
