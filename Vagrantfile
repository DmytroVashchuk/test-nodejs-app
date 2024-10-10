Vagrant.configure("2") do |config|

  # Налаштування для jenkins-master
  config.vm.define "jenkins-masterr" do |master|
    master.vm.box = "ubuntu/bionic64"

    # Налаштування мережі для доступу з публічної мережі
    master.vm.network "public_network", bridge: "Realtek RTL8821CE 802.11ac PCIe Adapter"

    # Для теперішнього етапу без автоматичної інсталяції
    # Можна вручну інсталювати Jenkins пізніше через SSH
  end

  # Налаштування для jenkins-worker
  config.vm.define "jenkins-worker" do |worker|
    worker.vm.box = "ubuntu/bionic64"

    # Налаштування мережі для доступу з публічної мережі
    worker.vm.network "public_network", bridge: "Realtek RTL8821CE 802.11ac PCIe Adapter"

    # Для теперішнього етапу без автоматичної інсталяції
    # Можна вручну інсталювати Docker та Jenkins worker пізніше через SSH
  end
end
