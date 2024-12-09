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
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && apt-get update \
    && apt-get install -y sudo \
    && echo 'kasm-user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
    && rm -rf /var/lib/apt/list/* \
    && chown 1000:0 $HOME \
    && $STARTUPDIR/set_user_permission.sh $HOME \
    && sudo apt-get install -y gedit \
    && sudo apt install -y iputils-ping \
    && sudo apt-get install -y bind9 \
    && sudo apt-get install -y dnsutils \
    && sudo rndc-confgen -a \
    # apache2 for experiment 2
    && sudo apt-get install -y apache2 \
    # wireshark for experiment 2
    && apt install -y wireshark \
    && sudo apt-get install -y python3-pip python3-dev \
    && sudo echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.bashrc \
    && exec bash \
    && source ~/.bashrc

######### End Customizations ###########
ENV HOME=/home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000