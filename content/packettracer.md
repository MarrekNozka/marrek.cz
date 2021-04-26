Title: T
Date: 2020-02-11 11:55
Category: Blog
Tags: Cisco 
Slug: packat-tracer-7.3.0
Author: Marek Nožka
Summary: Jak jsem instaloval Packet Trace 7.3.0 na Devuan GNU Linux
Status: draft

1.

Stáhnu deb balíček z [](https://netacad.com) a nainstaluju
  
  apt-get install /tmp/PT/PacketTracer_730_amd64.deb

2.

  cd /opt/pt/bin

3. 

  ./PacketTracer7
  ./PacketTracer7: error while loading shared libraries: libjpeg.so.8: cannot open shared object file: No such file or directory


4. 
  * https://packages.ubuntu.com/search?suite=bionic&arch=arm64&mode=exactfilename&searchon=contents&keywords=libjpeg.so.8
  * https://packages.ubuntu.com/bionic/libjpeg-turbo8
   
  
  dpkg-source -x libjpeg-turbo_1.5.2-0ubuntu5.18.04.3.dsc
  cd libjpeg-turbo-1.5.2
  dpkg-buildpackage -rfakeroot -b -uc -us -j

  dpkg -x libjpeg-turbo8_1.5.2-0ubuntu5.18.04.3_amd64.deb /tmp/turbo
  cp -a /tmp/turbo/usr/lib/x86_64-linux-gnu/libjpeg.so.8 /opt/pt/bin


