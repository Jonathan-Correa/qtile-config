#!/usr/bin/bash
resp=$(echo -e "Turn off\nLog out\nRestart" | dmenu -i -fn "Ubuntu Bold-11" -nb "#000000" -sb "#ffaa3b" -nf "#ffffff") 

case "$resp" in
  "Turn off") exec poweroff ;;
  "Log out") exec pkill -u $USER ;;
  "Restart") exec reboot ;;
  *) echo "Cualquier otra cosa" ;;
esac
