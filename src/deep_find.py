def deep_find(
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
        path = path.split(token)
        if path == ['']:
            path = None
        result = __rec_helper(obj, path)
    except Exception as e:
        if raise_err:
            raise e
        if default_if_err is not None:
            return default_if_err

    if result is not None:
        return result

    return default_return


def __rec_helper(obj: any, path: [str]):
    if not path:
        return obj

    current_path = path.pop(0)

    if isinstance(obj, dict):
        return __rec_helper(obj.get(current_path), path)

    if isinstance(obj, list):
        if current_path == '*':
            return [__rec_helper(sub_obj, path.copy()) for sub_obj in obj]
        if current_path == '?':
            for sub_obj in obj:
                result = __rec_helper(sub_obj, path.copy())
                if result is not None:
                    return result
            return None
        current_path_index = int(current_path)
        if current_path_index >= len(obj):
            return None
        return __rec_helper(obj[current_path_index], path)

    return None
