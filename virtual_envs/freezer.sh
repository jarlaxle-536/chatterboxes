#!/bin/bash
for env in dev test prod
do
src="${env}/bin/activate";
source $src;
pip freeze > "requirements_${env}.txt";
deactivate;
done
