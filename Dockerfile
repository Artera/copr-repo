FROM centos:7

RUN yum update -y
RUN yum install -y pigz createrepo mock rpmdevtools deltarpm rpm-sign sudo
RUN useradd -u 1000 -G mock builder
RUN echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN install -g mock -m 2775 -d /var/cache/mock
RUN echo "config_opts['cache_topdir'] = '/var/cache/mock'" >> /etc/mock/site-defaults.cfg

COPY bin/quick-build /usr/local/bin/quick-build
COPY rpmmacros /home/builder/.rpmmacros
COPY RPM-GPG-KEY-remi /etc/pki/mock/RPM-GPG-KEY-remi

VOLUME /home/builder/rpmbuild /home/builder/.gnupg /var/cache/mock
USER builder
ENV HOME=/home/builder
ENTRYPOINT ["/usr/local/bin/quick-build"]
