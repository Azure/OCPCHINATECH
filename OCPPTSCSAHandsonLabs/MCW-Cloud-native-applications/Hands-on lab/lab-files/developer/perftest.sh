host="fabmedical-[SUFFIX].documents.azure.com"
username="fabmedical-[SUFFIX]"
password="[PASSWORD]"
dbname="contentdb"
port="10255"

for i in {1..250}; do
    mongo $host:$port/$dbname \
        -u $username -p $password \
        --ssl --sslAllowInvalidCertificates \
        --eval 'db.sessions.insert({"title":"Perf Test"})' &
done