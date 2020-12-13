# Podman images
Images with Gentoo stage3 used in molecule with some packages preinstalled to speed up development and testing.

As of now I don't have a container registry so molecule expects that they are build locally.

```sh
podman build -f stage3-amd64 -t stage3-amd64
podman build -f <role-name> -t <role-name>
```
