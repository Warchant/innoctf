FROM fedora:24

RUN dnf upgrade -y && dnf install -y rust cargo && mkdir -p /srv/rustyserver

EXPOSE 8765
ADD rustyserver /srv/rustyserver
WORKDIR /srv/rustyserver/
RUN cargo build --release

CMD ["cargo", "run", "--release"]
