# check if sudo
if [ $(id -u) -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# run and connect containers
# expose port 6901 for attacker
docker run --name attacker --cap-add=NET_ADMIN --privileged --rm -d --shm-size=1024m -p 6901:6901 -e VNC_PW=password xjtuns_exp4_3:latest
# expose port 6902 for victim in a new terminal
docker run --name victim --cap-add=NET_ADMIN --privileged --rm -d --shm-size=1024m -p 6902:6901 -e VNC_PW=password xjtuns_exp4_3:latest

# show container ip
echo "Attacker IP: "
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker
echo "Victim IP: "
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' victim

# ask for execution completion
echo "Press any key to continue..."

read -p "Press any key to continue..." key

# stop and remove containers
docker stop attacker victim