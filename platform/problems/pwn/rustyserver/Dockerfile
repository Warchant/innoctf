FROM fedora

RUN dnf upgrade -y && dnf install -y rust cargo && mkdir -p /srv/rustyserver

EXPOSE 8765
WORKDIR /srv/rustyserver/
ADD rustyserver /srv/rustyserver
RUN cargo build --release

CMD ["cargo", "run", "--release"]
