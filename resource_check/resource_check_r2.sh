#!/usr/local/bin/zsh

dir="/Users/sunao/workspace/github/doc/vutm/20190611"
#echo $dir

python3 resource_check_r2.py $dir/upao01karaga-nfvi
python3 resource_check_r2.py $dir/upao03karaga-nfvi
python3 resource_check_r2.py $dir/upao05karaga-nfvi
python3 resource_check_r2.py $dir/upao07karaga-nfvi
python3 resource_check_r2.py $dir/uspao01karaga-nfvi
python3 resource_check_r2.py $dir/upao01naniwa-nfvi





