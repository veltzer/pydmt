#!/bin/sh
if [ -n "${PYCHARM_HOME}" ]
then
	${PYCHARM_HOME}/bin/inspect.sh $PWD .idea/inspectionProfiles/profiles_settings.xml inspections
else
	echo "varible 'PYCHARM_HOME' is not set"
fi
