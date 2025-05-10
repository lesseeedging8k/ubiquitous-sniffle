#!/bin/bash
quotes=("Stay hungry, stay foolish." "Code is like humor." "First, solve the problem." "There is no cloud...")
echo "💬 $(shuf -n1 -e "${quotes[@]}")"
