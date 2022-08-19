---
title:
created: 2021-07-30T17:19:55 (UTC -04:00)
tags: []
source: https://askubuntu.com/questions/763994/screen-times-out-in-i3-wm
author: nooreennooreen
        
            36311 gold badge33 silver badges44 bronze badges
---

# i3 wm - Screen times out in i3 WM - Ask Ubuntu

> ## Excerpt
> I love i3 for obvious reasons (light, maxing screen size, ability to customize). However, my screen times out after five minutes of inactivity. I would like to turn this off, how?

I've got i3 on u...

---
X.org has some basic screen saver functionality as well as energy saving features. Most likely either or both are responsible for the described behavior.

The settings for both can be viewed and changed with the `xset` tool (from the `x11-xserver-utils` package). `xset q` displays the current settings in the sections _Screen Saver_ and _DPMS (Energy Star)_.

You can disable the screen saver feature with:

```
xset s off
```

The power saving feature can be turned off with

```
xset -dpms
```

With these settings the screen should no longer turn off or blank automatically until you reboot your machine.

___

If your main concern is that 5 minutes are to short, you can also just raise the limits for that. To enable the screen saver only after 15 minutes (900 seconds) idle time, set the timeout accordingly with

```
xset s 900
```

To turn off the monitor after 20 minutes of idling run

```
xset dpms 0 0 1200
```

The two `0` values disable _standby_ and _suspend_ respectively, while `1200` sets the timeout for _off_ to 20 minutes. (I usually do not use _standby_ or _suspend_ because there seems to be no difference between the three modes on modern TFT-displays.) Setting these values also enables _DPMS_, so you do not need to explicitly run `xset +dpms`.
