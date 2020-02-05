FROM centos:latest
MAINTAINER Mahmoud Alkelany "mmahmoh@gmail.com"
RUN yum -y install epel-release 
#RUN yum -y install python-pip 
RUN yum install -y python-redis python-flask python-cherrypy python-devel gcc gcc-c++ glibc-devel make && yum clean all 
COPY . /app
WORKDIR /app
#RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/bin/cherryd","-d","-c","conf","-i","app"]
