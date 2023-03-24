![logo](docs/logo-small.png)

This repository (udocker_tools) contains modules and execution engines for udocker.

udocker is a basic user tool to execute simple docker containers in user
space without requiring root privileges. Enables download and execution
of docker containers by non-privileged users in Linux systems where
docker is not available. It can be used to pull and execute docker
containers in Linux batch systems and interactive clusters that are
managed by other entities such as grid infrastructures or externally
managed batch or interactive systems.

## Information and usage

The repository contains the following:

* Directory `utils` has several scripts both in bash and python.
* Directory `engines` contains the current version of binaries and libraries
  of the execution engines.
* Directory `tarballs` contains the tarball of each binary or library.

The bash script `utils/make-tar.sh` makes the tarballs and produces a CSV `flist.csv`
with the filename and corresponding sha256sum. This file was edited to complete with the other
columns to `flist-keep.csv`

The python script `utils/make-meta.py` reads `flist-keep.csv` and produces the json file
`metadata.json`, containing all information needed for the udocker commands to install one
or more modules.

## How to update this repository

The udocker tools tarball are build in the following repository:

* <https://github.com/jorge-lip/udocker-builds>

Execute the following script, it downloads a given version of the udocker tools tarball, unpacks it,
tar and zip each individual binary and lib, calculates the sha256 checksum, and puts it into the
repository directory  `tarballs/`, it also produces a new flist.csv:

```bash
cd utils
./make-tar.sh 1.2.9
```

## Contributing

See: [Contributing](CONTRIBUTING.md)

## Licensing

Redistribution, commercial use and code changes must regard all licenses
shipped with udocker. These include the [udocker_tools license](LICENSE) and the
individual licenses of the external tools and libraries packaged for use
with udocker.

## Acknowledgements and further documentation

* Docker: <https://www.docker.com/>
* PRoot:
  * <https://proot-me.github.io/>
  * <https://github.com/jorge-lip/proot-udocker>
* Fakechroot:
  * <https://github.com/dex4er/fakechroot/wiki>
  * For libfakechroot-glibc: <https://github.com/jorge-lip/libfakechroot-glibc-udocker>
  * For libfakechroot-musl: <https://github.com/jorge-lip/libfakechroot-musl-udocker>
* runC <https://runc.io/>
* crun <https://github.com/containers/crun>
* Singularity <https://www.sylabs.io/>
* PatchELF:
  * <https://github.com/NixOS/patchelf>
  * <https://github.com/jorge-lip/patchelf-udocker>
* Open Container Initiative <https://www.opencontainers.org/>
* EGI-ACE <https://www.egi.eu/projects/egi-ace/>
* EOSC-Synergy <https://www.eosc-synergy.eu/>
* LIP [https://www.lip.pt](https://www.lip.pt/?section=home&page=homepage&lang=en)
* INCD [https://www.incd.pt](https://www.incd.pt/?lang=en)
