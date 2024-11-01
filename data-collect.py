#!/usr/bin/env python3

import numpy as np
import csv

# Standard Deviation of Packets
packetcsv = np.genfromtxt('data-packets.csv', delimiter=",")
packets = packetcsv[:,0]
stdevpack = np.std(packets)

# Standard Deviation of Bytes
bytecsv = np.genfromtxt('data-bytes.csv', delimiter=",")
bytes_data = bytecsv[:,0]
stdevbyte = np.std(bytes_data)

# Number of Source IPs
nbip = len(set(bytecsv[:, 0]))

# Number of Flow Entries
nbfl = len(bytecsv)

# Number of Interactive Flow Entries
with open('data-ip-src.csv', 'r') as t1, open('data-ip-dst.csv', 'r') as t2:
    src_ips = set(t1.readlines())
    dst_ips = set(t2.readlines())

interflow_ips = src_ips.intersection(dst_ips)
interflow = len(interflow_ips) / nbip

# Creating headers
header = ["SSIP", "Stdevpack", "Stdevbyte", "NbFlow", "NbIntFlow"]

# Creating Training Data For Normal Traffic
smart = [nbip, stdevpack, stdevbyte, nbfl, interflow]

# Writing to CSV
with open('Live.csv', 'w', newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(header)
    writer.writerow(smart)


