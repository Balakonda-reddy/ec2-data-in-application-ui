
import boto3
import csv 

from pprint import pprint

ec2_client = boto3.client(service_name='ec2')

collect_all_regions = []

for each_region in ec2_client.describe_regions()['Regions']:
    collect_all_regions.append(each_region['RegionName'])
print(collect_all_regions)

fo=open('ec2_list_all.csv','w',newline='')
data_obj = csv.writer(fo)
data_obj.writerow(['sno','Instance_Id'])

cnt =1

for each_region in collect_all_regions:
    ec2_resou=boto3.resource(service_name='ec2',region_name = each_region)
    for each_ins_in_reg in ec2_resou.instances.all():
        data_obj.writerow([cnt,each_ins_in_reg.instance_id])
        cnt+=1

fo.close()
