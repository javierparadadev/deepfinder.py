# Deep finder

[![GitHub](https://img.shields.io/github/license/parada3desu/deepfinder.py)](https://github.com/parada3desu/deepfinder.py/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/deepfinder)](https://pypi.org/project/deepfinder/)
[![GA](https://github.com/parada3desu/deepfinder.py/workflows/tests/badge.svg)](https://github.com/parada3desu/deepfinder.py/actions/workflows/test.yml)

Search attributes easily within structures of type dictionary, list and embedded substructures with simple format 'dict.users.0.name'.

## Getting Started

### Installation

```Shell
  pip install deepfinder
```

### Usage

#### Basic sample

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'links': {
        'pokehub': '@ash',
    },
}
print(deep_find(user, 'links.pokehub'))
# output: '@ash'
```

#### List sample

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'pokemons': [{
        'name': 'pikachu',
    }, {
        'name': 'charmander',
    }]
}
print(deep_find(user, 'pokemons.0.name'))
# output: 'pikachu'
```

#### List all result sample

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'pokemons': [{
        'name': 'pikachu',
    }, {
        'name': 'charmander',
    }]
}
print(deep_find(user, 'pokemons.*.name'))
# output: ['pikachu', 'charmander']
```

#### List and not null result sample

```python
from deepfinder import deep_find
user: dict = {
    'name': 'ash',
    'pokemons': [{
        'name': 'pikachu',
    }, {
        'name': 'charmander',
        'ball': 'superball',
    }]
}
print(deep_find(user, 'pokemons.?.ball'))
# output: 'superball'
```

### Use custom dict and list

```python
from deepfinder.entity import DeepFinderDict
user: dict = DeepFinderDict({
    'name': 'ash',
    'pokemons': [{
        'name': 'pikachu',
    }, {
        'name': 'charmander',
        'ball': 'superball',
    }]
})
print(user.deep_find('pokemons.?.ball'))
# output: 'superball'
```

```python
from deepfinder.entity import DeepFinderList
users: list = DeepFinderList([{
    'name': 'ash',
    'pokemons': [{
        'name': 'pikachu',
    }, {
        'name': 'charmander',
        'ball': 'superball',
    }]
}])
print(users.deep_find('0.pokemons.?.ball'))
# output: 'superball'
```

