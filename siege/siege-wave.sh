# Siege wave script

echo "$1 concurrent users for 10 seconds"
echo "POST data"
siege -c$1 -r10 -d1 --content-type="application/json" -f urls.txt
# Clean up
echo "DELETE data (1 concurrent user)"
siege -c1 -r1 -d1 'http://web:5000/ DELETE'
echo "Sleeping for 5 seconds to process any queued requests"
sleep 5
