from __future__ import annotations

from typing import Any


def deep_find(
    obj: Any,
    path: str,
    token: str = '.',
    default_return: Any = None,
) -> Any:
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
    result = _rec_helper(obj, path)

    if result is not None:
        return result

    return default_return


def _rec_helper(obj: Any, path: list[str]) -> Any:
    if not path:
        return obj

    current_path = path.pop(0)

    if isinstance(obj, dict):
        return _rec_helper(obj.get(current_path), path)

    if isinstance(obj, set):
        obj = list(obj)

    if isinstance(obj, list):
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

    if hasattr(obj, '__dict__') and current_path in vars(obj):
        return _rec_helper(vars(obj)[current_path], path)

    return
