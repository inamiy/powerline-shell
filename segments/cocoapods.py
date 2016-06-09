import subprocess

def add_cocoapods_segment(powerline):
    ret = subprocess.call('diff "Podfile.lock" "Pods/Manifest.lock" &> /dev/null', shell = True)
    if ret != 1:
        return
    fg = Color.CMD_FAILED_FG
    bg = Color.CMD_FAILED_BG
    powerline.append(' %s pod ' % u'\u2717', fg, bg)

