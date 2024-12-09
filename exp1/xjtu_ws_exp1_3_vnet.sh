# check if sudo
if [ $(id -u) -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# create a bridge network
# docker network create -d bridge \
#     --subnet 172.25.0.0/24 \
#     --gateway 172.25.0.1 \
#     vnet

# run and connect containers
# expose port 6901 for server
docker run --name server -itd xjtuns_exp1:latest
# expose port 6902 for client in a new terminal
# docker run --name client --cap-add=NET_ADMIN --privileged --rm -d --shm-size=512m -p 6902:6901 -e VNC_PW=password kswebxjtuwebsecurity:latest
docker run --name client -itd xjtuns_exp1:latest
# expose port 6903 for simulating DNS server
# docker run --name dns --cap-add=NET_ADMIN --privileged --rm -d --shm-size=512m -p 6903:6901 -e VNC_PW=password kswebxjtuwebsecurity:latest

# connect containers to the bridge network
# server ip: 172.25.0.2
# docker network connect --ip 172.17.0.2 bridge server
# client ip: 172.25.0.3
# docker network connect --ip 172.17.0.3 bridge client
# dns ip: 172.25.0.4
# docker network connect --ip 172.25.0.4 vnet dns

# ask for execution completion
echo "Press any key to continue..."

read -p "Press any key to continue..." key

# stop and remove containers
docker stop server client # dns
docker rm server client
# remove bridge network
# docker network rm vnet