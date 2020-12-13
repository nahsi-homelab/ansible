FROM docker.io/gentoo/portage:latest as portage
FROM docker.io/gentoo/stage3-amd64:latest

COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo
RUN emerge -qv app-portage/gentoolkit
