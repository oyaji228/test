#!/usr/local/bin/zsh

dir="/Users/sunao/workspace/github/doc/vutm/uspao01karaga-nfvi_20190326"
#echo $dir

python3 resource_check_r2.py $dir/upao01karaga-nfvi_20190326.log
python3 resource_check_r2.py $dir/upao01naniwa-nfvi_20190326.log
python3 resource_check_r2.py $dir/upao03karaga-nfvi_20190326.log
python3 resource_check_r2.py $dir/upao05karaga-nfvi_20190326.log
python3 resource_check_r2.py $dir/upao07karaga-nfvi_20190326.log
python3 resource_check_r2.py $dir/uspao01karaga-nfvi_20190326.log





