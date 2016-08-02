# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.network "private_network", type: "dhcp"

  config.ssh.forward_agent = true

  config.vm.synced_folder ".", "/home/vagrant/sync", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/rpmbuild", :type => "nfs", :nfs_version => 4, :nfs_udp => false
  config.vm.synced_folder "Vagrant/roots", "/srv/salt", :type => "nfs", :nfs_version => 4, :nfs_udp => false
  config.vm.synced_folder "Vagrant", "/srv/vagrant", :type => "nfs", :nfs_version => 4, :nfs_udp => false

  config.vm.provider "virtualbox" do |vb|
    vb.linked_clone = true
    vb.memory = 2048
  end

  config.vm.provider "libvirt" do |domain|
    domain.memory = 2048
    domain.volume_cache = "none"
  end

  config.vm.provision :salt, run: "always" do |salt|
    salt.masterless = true
    salt.minion_config = "Vagrant/minion"
    salt.minion_id = "vagrant"
    salt.run_highstate = true
    salt.bootstrap_options = "-p git"
    salt.log_level = 'warning'
    salt.verbose = true
    salt.colorize = true
  end
end
