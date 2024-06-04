#!/bin/bash
# set -x

CERT_DIR="./certs"
CA_KEY_PATH="./certs/ca/RootCA.key"
CA_CERT_PATH="./certs/ca/RootCA.crt"
CA_CONF_PATH="./certs/ca/RootCA.conf"

# Function to check if a string is an IP address
is_ip() {
    # Regex pattern to match an IP address
    local ip_pattern="^([0-9]{1,3}\.){3}[0-9]{1,3}$"
    
    if [[ $1 =~ $ip_pattern ]]; then
        echo "{$1} is an IP address"
        return 0
    else
        echo "{$1} is Not an IP address"
        return 1
    fi
}

ca() {
    if [ -f "$CA_CONF_PATH" ] && [ -d "$CERT_DIR" ]; then
        openssl req -x509 -nodes -new -keyout "$CA_KEY_PATH" -out "$CA_CERT_PATH" -config "$CA_CONF_PATH"
        openssl x509 -text -noout -in "$CA_CERT_PATH"
    else
        echo "$CA_CONF_PATH not exist!"
        exit 1
    fi
}

sign() {
    if [ -f "$CA_KEY_PATH" ] && [ -f "$CA_CERT_PATH" ] && [ -d "$CERT_DIR" ]; then
        # Check the number of arguments
        if [ $# -gt 0 ]; then
            echo "You supplied domain: $@"
            SAN_LIST="[SAN]\nsubjectAltName="

            # Loop
            for arg in "$@"; do
                is_ip "$arg"
                local is_ip_result=$?
                if [ $is_ip_result -eq 0 ]; then
                    san="IP:$arg"
                else
                    san="DNS:$arg"
                fi
                SAN_LIST="$SAN_LIST$san,"
                DOMAIN_NAME=$arg
            done

            # Remove the last character if it is ","
            if [[ "${SAN_LIST: -1}" == "," ]]; then
                SAN_LIST="${SAN_LIST:0:-1}"
            fi
            printf $SAN_LIST
        else
            echo "Default domains: 'DNS:localhost, DNS:*.localhost, IP:127.0.0.1' will be added to cert"
            DOMAIN_NAME="127.0.0.1"
            SAN_LIST="[SAN]\nsubjectAltName=DNS:localhost, DNS:*.localhost, IP:127.0.0.1"
            printf $SAN_LIST
        fi
        printf "\n\n"

        SUBJECT="/C=HK/ST=HongKong/L=HongKong/O=MTR CORP/OU=IT Deparment/CN=$DOMAIN_NAME Self-Signed/emailAddress=admin@example.com"

        SERVER_KEY="$CERT_DIR/$DOMAIN_NAME.key"
        SERVER_CERT="$CERT_DIR/$DOMAIN_NAME.crt"
        SERVER_CSR="$CERT_DIR/$DOMAIN_NAME.csr"

        openssl req -new -nodes -newkey rsa:2048 -keyout "$SERVER_KEY" -out "$SERVER_CSR" -subj "$SUBJECT" -reqexts SAN -config <(echo -e "$SAN_LIST")

        openssl x509 -req -sha256 -days 3650 -in "$SERVER_CSR" -CA "$CA_CERT_PATH" -CAkey "$CA_KEY_PATH" -CAcreateserial -copy_extensions copyall -out "$SERVER_CERT"

        echo "new TLS self-signed certificate created"
        echo "view $SERVER_CERT:"
        openssl x509 -text -noout -in "$SERVER_CERT"

        openssl verify -verbose -CAfile "$CA_CERT_PATH" "$SERVER_CERT"

        echo "Generet Certificate Finished at:"
        echo "server $DOMAIN_NAME cert: $SERVER_CERT"
        echo "server $DOMAIN_NAME key: $SERVER_KEY"

    else

        echo "$CA_KEY_PATH and $CA_CERT_PATH not exist!"
        exit 1

    fi
}

main() {
    case "$1" in
    ca)
        ca
        ;;
    sign)
        sign "${@:2}"   # Pass all arguments except the first one!
        ;;
    *)
        echo "Invalid subcommand. Usage:
            $0 ca
            $0 sign {ipaddress1|dns1}, {ipaddress2|dns2}, ...
            "
        exit 1
        ;;
    esac
}

main "$@"
