#!/bin/bash

# read the curl command from the input file
curl_cmd=$(cat input.txt)

# add proxy argument to curl command if it's not already present
if [[ $curl_cmd != *"--proxy 127.0.0.1:8080"* ]]; then
  curl_cmd="$curl_cmd --proxy 127.0.0.1:8080"
  echo "Proxy argument added to curl command."
fi

# prompt for the string to be replaced
echo "Enter the string to be replaced:"
read target_str

# prompt for the start and end values for the replacement range
echo "Enter the start value for the replacement range:"
read start_value
echo "Enter the end value for the replacement range:"
read end_value

# generate parallel curl requests with the target string replaced with the replacement values for each request
for (( i=$start_value; i<=$end_value; i++ ))
do
  # replace the target string with the current value
  cmd="${curl_cmd//$target_str/$i}"

  # execute the curl request in the background
  eval "$cmd" &

done

# wait for all the background jobs to finish
wait
