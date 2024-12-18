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
    # basic tools
    && sudo apt-get install -y gedit \
    && sudo apt install -y iputils-ping \
    # wireshark
    && apt install -y wireshark \
    # ettercap
    && sudo apt-get install ettercap-common -y \
    # drift net
    && sudo apt-get install driftnet -y

######### End Customizations ###########
ENV HOME=/home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000