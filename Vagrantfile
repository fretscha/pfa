# -*- mode: ruby -*-
# vi: set ft=ruby noai:sw=2 ts=2 tw=78

Vagrant.configure(2) do |config|
  config.vm.box = "vivid/server"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/vivid/current/vivid-server-cloudimg-amd64-vagrant-disk1.box"
  #config.vm.network "private_network", ip: "172.20.1.51"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 5432, host: 15432

  config.cache.enable :apt
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope       = :machine # or :box
    config.cache.auto_detect = false
  end

  config.vm.provision :shell, :path => "scripts/ubuntu_packages.sh"
  config.vm.provision :shell, :path => "scripts/python_packages.sh"
  config.vm.provision :shell, :path => "scripts/postgres.sh"
  config.vm.provision :shell, :path => "scripts/grunt.sh"
  config.vm.provision :shell, :path => "scripts/celery.sh"
  config.vm.provision :shell, :path => "scripts/django_env.sh"
end
