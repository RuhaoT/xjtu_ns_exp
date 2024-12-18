# check if sudo
if [ $(id -u) -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# run and connect containers
# expose port 6901 for server
docker run --name server --cap-add=NET_ADMIN --privileged --rm -d --shm-size=1024m -p 6901:6901 -e VNC_PW=password xjtuns_exp4_1:latest
# expose port 6902 for client in a new terminal
# docker run --name client --cap-add=NET_ADMIN --privileged --rm -d --shm-size=512m -p 6902:6901 -e VNC_PW=password xjtuns_exp2:latest

# show container ip
echo "Server IP: "
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server
# echo "Client IP: "
# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client

# ask for execution completion
echo "Press any key to continue..."

read -p "Press any key to continue..." key

# stop and remove containers
docker stop server # client # dns