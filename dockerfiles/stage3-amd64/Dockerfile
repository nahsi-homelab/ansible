FROM docker.io/gentoo/portage:latest as portage
FROM docker.io/gentoo/stage3-amd64:latest

COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo
RUN echo 'rc_provide="loopback net"' >> /etc/rc.conf &&\
    sed -i 's/cgroup_add_service /# cgroup_add_service /g' /lib/rc/sh/openrc-run.sh &&\
    emerge -qv app-portage/gentoolkit &&\
    USE="-bindist" emerge -qv --changed-use -1 dev-libs/openssl net-misc/openssh

CMD /sbin/openrc-init
