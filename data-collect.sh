#!/bin/bash
for i in {1..2000}
do
sudo ovs-ofctl dump-flows s6 > new-packets
grep "nw_src" new-packets > data.csv
cat data.csv | awk -F"," '{print $4}' | awk -F"=" '{print $2","}' > data-packets.csv
cat data.csv | awk -F"," '{print $5}' | awk -F"=" '{print $2","}' > data-bytes.csv
cat data.csv | awk -F"," '{print $15}' | awk -F"=" '{print $2","}' > data-ip-src.csv
cat data.csv | awk -F"," '{print $16}' | awk -F"=" '{print $2","}' > data-ip-dst.csv

sudo python3 data-collect.py
sudo ovs-ofctl del-flows s6
echo $i
sudo python3 svm.py
r=$(awk '{print $0;}' Result.txt)
if [ $r -eq 1 ]
then
echo "network is under attack!!"
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.1,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.2,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.3,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.4,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.5,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.6,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.7,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.8,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.9,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.10,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.11,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.12,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.13,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.14,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.15,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.16,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.17,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.18,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.19,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_src=10.0.0.20,priority=60000,actions=output:2
sudo ovs-ofctl add-flow s6 ip,nw_dst=10.0.0.21,priority=50000,actions=drop

else
	echo "Normal Traffic"
fi
sleep 3
done

