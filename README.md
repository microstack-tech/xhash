# XHash

[![readme style standard](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![GitPOAP Badge](https://public-api.gitpoap.io/v1/repo/microstack-tech/xhash/badge)](https://www.gitpoap.io/gh/microstack-tech/xhash)

> C/C++ implementation of XHash – the Parallax Proof of Work algorithm


## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Optimizations](#optimizations)
- [Maintainer](#maintainer)
- [License](#license)


## Install

Build from source using CMake.

```sh
mkdir build
cd build
cmake ..
cmake --build .
```

## Usage

See [xhash.hpp] for a list of exported functions and documentation.


## Optimizations

This section describes the modifications applied
in this library in relation to [Ethash reference implementation](https://github.com/ethereum/wiki/wiki/Ethash).

The XHash specification can be found in the [Parallax technical documentation](https://docs.parallaxchain.org/parallax-protocol/foundational-topics/consensus/algorithms/xhash).

The library contains a set of micro-benchmarks. Build and run the `xhash-bench`
tool.

## Maintainer

Andre Patta [@andrepatta]

## License

Licensed under the [Apache License, Version 2.0].


[@chfast]: https://github.com/chfast
[Apache License, Version 2.0]: LICENSE
[xhash.hpp]: include/xhash/xhash.hpp
