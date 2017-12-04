#!/bin/sh
export PYCHARM_HOME=${HOME}/install/pycharm
${PYCHARM_HOME}/bin/inspect.sh . .idea/inspectionProfiles/profiles_settings.xml inspections
