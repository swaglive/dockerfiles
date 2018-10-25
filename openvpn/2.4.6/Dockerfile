FROM        kylemanna/openvpn:2.4 as openvpn

###

FROM        alpine:3.8

ENV         OPENVPN /etc/openvpn
ENV         EASYRSA /usr/share/easy-rsa
ENV         EASYRSA_PKI $OPENVPN/pki
ENV         EASYRSA_VARS_FILE $OPENVPN/vars
ENV         EASYRSA_CRL_DAYS 3650

EXPOSE      1194/udp

CMD         ["ovpn_run"]

RUN         apk add --no-cache \
                openvpn=2.4.6-r3 \
                iptables \
                bash \
                easy-rsa && \
            ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin

COPY        --from=openvpn /usr/local/bin /usr/local/bin
RUN         chmod a+x /usr/local/bin/*
