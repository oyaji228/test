#!/usr/local/bin/zsh

#dir="/Users/sunao/workspace/github/doc/vutm/20190611"
dir="/Users/sunao/workspace/github/doc/vutm/20190627"

#echo $dir

# set
python3 resource_check_r2.py $dir/upao01naniwa-nfvi-set.txt
python3 resource_check_r2.py $dir/upao01karaga-nfvi-set.txt
python3 resource_check_r2.py $dir/upao03karaga-nfvi-set.txt
python3 resource_check_r2.py $dir/upao05karaga-nfvi-set.txt
python3 resource_check_r2.py $dir/upao07karaga-nfvi-set.txt
python3 resource_check_r2.py $dir/upao09karaga-nfvi-set.txt
python3 resource_check_r2.py $dir/upao11karaga-nfvi-set.txt
python3 resource_check_r2.py $dir/uspao01karaga-nfvi-set.txt


# xml

#python3 resource_check_r2.py $dir/upao01karaga-nfvi
#python3 resource_check_r2.py $dir/upao03karaga-nfvi
#python3 resource_check_r2.py $dir/upao05karaga-nfvi
#python3 resource_check_r2.py $dir/upao07karaga-nfvi
#python3 resource_check_r2.py $dir/uspao01karaga-nfvi
#python3 resource_check_r2.py $dir/upao01naniwa-nfvi





