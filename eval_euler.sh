python script/euler2eulers.py
python script/sols2json.py

# change input $1 to string, for example, 1->"001", 35->"035", store result to variable n

n=$1
sn=$(printf "%03d" "$n")
python code/check_euler.py --problem "./data/eulers/euler"$sn".ped" --input "./data/euler_sol.json" --output "./result/euler"$sn"_res.json"