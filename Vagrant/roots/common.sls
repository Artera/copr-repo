zsh:
  pkg.installed: []
  git.latest:
    - name: https://github.com/robbyrussell/oh-my-zsh.git
    - target: /home/vagrant/.oh-my-zsh
    - rev: master
    - depth: 1
    - user: vagrant

/home/vagrant/.oh-my-zsh:
  file.directory:
    - user: vagrant
    - mode: 700
    - require:
      - git: zsh

/home/vagrant/.zshrc:
  file.managed:
    - source: salt://zshrc
    - user: vagrant
    - mode: 600

vagrant:
  user.present:
    - shell: /bin/zsh
    - require:
      - pkg: zsh

selinux:
  cmd.run:
    - name: setenforce Permissive
    - unless: getenforce | grep -q Permissive

utils:
  pkg.installed:
    - pkgs:
      - yum-utils
      - pigz
      - createrepo
      - mock
      - rpmdevtools
      - deltarpm
      - rpm-sign

timedatectl set-timezone Europe/Rome:
  cmd.run:
    - unless: "timedatectl status | grep -q 'Time zone: Europe/Rome'"
