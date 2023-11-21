# Wait for db to initialize
echo "Waiting for db to initialize"
sleep 15

# 10 concurrent users
sh siege-wave.sh 10
# 25 concurrent users
sh siege-wave.sh 25
# 50 concurrent users
sh siege-wave.sh 50
# 100 concurrent users
sh siege-wave.sh 100
# 250 concurrent users
# sh siege-wave.sh 250
