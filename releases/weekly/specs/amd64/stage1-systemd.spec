subarch: amd64
target: stage1
version_stamp: systemd-@latest@
rel_type: systemd
profile: default/linux/amd64/13.0/systemd
snapshot: @latest@
source_subpath: systemd/stage3-amd64-systemd-latest
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
