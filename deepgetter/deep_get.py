def deep_get(
        obj: any,
        path: str,
        token: str = '.',
        default_return: any = None,
        default_if_err: any = None,
        raise_err: bool = False,
) -> any:
    """
        Description
        :param raise_err:
        :param default_if_err:
        :param default_return: default return if function raise an error or param is None.
        :param token: token to separate attributes.
        :param obj: obj in which find.
        :param path: path to wanted attribute.
        :return: found attribute.
    """
    result: any = None
    try:
        result = __rec_helper(obj, path.split(token))
    except Exception as e:
        if raise_err:
            raise e
        if default_if_err is not None:
            return default_if_err

    if result is not None:
        return result

    return default_return


def __rec_helper(obj: any, path: [str]):
    return 'any'
