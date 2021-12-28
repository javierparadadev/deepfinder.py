def deep_find(
        obj: any,
        path: str,
        token: str = '.',
        default_return: any = None,
) -> any:
    """
        Description
        :param default_return: default return if function raise an error or param is None.
        :param token: token to separate attributes.
        :param obj: obj in which find.
        :param path: path to wanted attribute.
        :return: found attribute.
    """
    path = path.split(token)
    if path == ['']:
        path = None
    result = __rec_helper(obj, path)

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

        if current_path in ['*?', '?*']:
            with_nones_results = [__rec_helper(sub_obj, path.copy()) for sub_obj in obj]
            clear_results = [obj for obj in with_nones_results if obj is not None]
            return clear_results

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

    if hasattr(obj, '__dict__') and current_path in obj.__dict__:
        return __rec_helper(obj.__dict__[current_path], path)

    return None
