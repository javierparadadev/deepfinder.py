from __future__ import annotations

from typing import Any, Iterable


def deep_find(
    obj: Any,
    path: str,
    path_token: str = '.',
    default: Any = None,
) -> Any:
    """
        Description
        :param default: default return if function raise an error or param is None.
        :param path_token: token to separate attributes.
        :param obj: obj in which find.
        :param path: path to wanted attribute.
        :return: found attribute.
    """
    path = path.split(path_token)
    if path == ['']:
        path = None
    result = _rec_helper(obj, path)

    if result is not None:
        return result

    return default


def _rec_helper(obj: Any, path: list[str]) -> Any:
    if not path:
        return obj

    current_path = path.pop(0)

    if isinstance(obj, dict):
        return _rec_helper(obj.get(current_path), path)

    if isinstance(obj, Iterable) and not isinstance(obj, str):
        obj = list(obj)

    if isinstance(obj, list):
        return _rec_list_helper(obj, path, current_path)

    if hasattr(obj, '__dict__') and current_path in vars(obj):
        return _rec_helper(vars(obj)[current_path], path)
    
    return


def _rec_list_helper(obj: list[Any], path: list[str], current_path: str):
    if current_path == '*':
        return [_rec_helper(sub_obj, path.copy()) for sub_obj in obj]

    if current_path in ['*?', '?*']:
        with_nones_results = [_rec_helper(sub_obj, path.copy()) for sub_obj in obj]
        clear_results = [obj for obj in with_nones_results if obj is not None]
        return clear_results

    if current_path == '?':
        for sub_obj in obj:
            result = _rec_helper(sub_obj, path.copy())
            if result is not None:
                return result
        return

    try:
        current_path_index = int(current_path)
    except ValueError as _:
        return
    if current_path_index >= len(obj):
        return
    return _rec_helper(obj[current_path_index], path)
