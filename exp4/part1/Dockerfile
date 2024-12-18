#Dockerfile
#sudo as root role.
 
FROM kasmweb/desktop:1.16.1-rolling-weekly
USER root
 
ENV HOME=/home/kasm-default-profile
ENV STARTUPDIR=/dockerstartup
ENV INST_SCRIPTS=$STARTUPDIR/install
WORKDIR $HOME
 
######### Customize Container Here ###########
ENV TZ=Asia/Shanghai

# copy xampp installer, DVWA folder, and burpsuite jar to home directory
COPY ./xampp-linux-x64-8.2.4-0-installer.run $HOME
COPY ./DVWA $HOME/DVWA
COPY ./burpsuite_community_v2024.10.3.jar $HOME

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && apt-get update \
    && apt-get install -y sudo \
    && echo 'kasm-user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
    && rm -rf /var/lib/apt/list/* \
    && chown 1000:0 $HOME \
    && $STARTUPDIR/set_user_permission.sh $HOME \
    # basic tools
    && sudo apt-get install -y gedit \
    && sudo apt install -y iputils-ping \
    # jdk environment for brupsuite
    && sudo apt-get install openjdk-21-jdk -y \
    # ca certificates
    && sudo apt-get install -y ca-certificates \
    # xmapp
    && chmod +x $HOME/xampp-linux-x64-8.2.4-0-installer.run \
    && echo -e "Y""Y""\n""Y" | $HOME/xampp-linux-x64-8.2.4-0-installer.run \
    # copy DVWA to /opt/lampp/htdocs
    && cp -r $HOME/DVWA /opt/lampp/htdocs \
    # start all xampp services
    && sudo /opt/lampp/lampp start \
    # wait for xampp to start
    && sleep 10 \
    # create a dvwa database in mysql
    && sudo /opt/lampp/bin/mysql -u root -e "CREATE DATABASE dvwa" \
    # create a dvwa user in mysql
    && sudo /opt/lampp/bin/mysql -u root -e "CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'p@ssw0rd'" \
    # grant all privileges to dvwa user
    && sudo /opt/lampp/bin/mysql -u root -e "GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost'" \
    # flush privileges
    && sudo /opt/lampp/bin/mysql -u root -e "FLUSH PRIVILEGES"

######### End Customizations ###########
ENV HOME=/home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000