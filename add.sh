#!/bin/bash
filename=$1
eval "$(touch $1)"
chmod u+x $1
echo "#!/bin/bash" > $1
nano $1
