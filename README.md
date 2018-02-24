# NABUI

Not Another Bettercap UI

---

## PREAMBLE

This project is very early in development, to a point where I normally wouldn't OSS it yet. But, I want people to be able to check it out if they want - since it is relatively straightforward and (what it does do) works(?) at this point.

There is still come pretty critical framework, structure and tons of refactoring I want to get written out and merged before I start taking an real contributions or anything like that. So, if you want to contribute to this project, hells yeahs and thank you in advance. But, maybe hold off a couple of weeks until I get my side sorted. Maybe shoot an issue or something like that if you think it's worth discussing. If you come across any actual bugs, or issues with installing/running on platform/setup $X, I would love to hear about that as soon as possible too.

I'll nuke this part of the readme once I get my base ready and am ready to start accepting PR's.

---

## INSTALL

have bettercap already running with the rest-api caplet (`bettercap -caplet rest-api.cap`). If bettercap isn't running locally, set BETTERCAP_URL. Even if it is set locally, you may have to set the interface ip for now.

```
pip3 install -r requirements
python3 nabui.py
```

Log in with the username `bcap` and password `bcap`.

---

Tested on Chrome and Linux, ymmv.

I will be pushing a lot to this over the next couple weeks in an effort to get it up to speed and be more usable than a kind of nice looking web interface. But, till then, this is what you're stuck with.