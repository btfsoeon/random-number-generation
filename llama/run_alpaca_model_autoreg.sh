#!/bin/bash

OUTPUT=stdout.txt
# N_MAX=(10 100 1000 10000 100000)

# for v_max in "${N_MAX[@]}"
# do
#     for j in {1..20}
#     do
#         # (./chat_mac < prompt.txt) |  awk '/def/{exit}1'
#         script -a ${v_max}_${OUTPUT} bash -c "echo -e \"Pick ten random numbers from 1-${v_max}.\n\" | ./chat_mac | awk '/def/{exit}1' | awk '/import/{exit}1'"
#     done

#     grep '>' ${v_max}_${OUTPUT}
# done

for j in {1..200}
do
    # (./chat_mac < prompt.txt) |  awk '/def/{exit}1'
    script -a ${v_max}_${OUTPUT} bash -c "echo -e \"Give me a list of uniform random numbers in the interval [0, 1]:\n\" | ./chat_mac | awk '/def/{exit}1' | awk '/import/{exit}1'"
done

grep '>' 1_${OUTPUT}
