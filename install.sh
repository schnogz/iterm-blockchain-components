
#!/bin/bash

set -e

iterm_scripts_dir="$HOME/Library/Application Support/iTerm2/Scripts/AutoLaunch"
mkdir -p "$iterm_scripts_dir"

echo Copying scripts to AutoLaunch folder $iterm_scripts_dir

for script in $(ls *.py); do
    echo Copying $script...
    cp $script "$iterm_scripts_dir/$script"
done
