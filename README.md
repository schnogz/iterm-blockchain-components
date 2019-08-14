# iterm-btc-status-bar-components
Custom Bitcoin (BTC) related status bar components for use with iTerm2

![overview](screenshots/overview.png)

## Installation & Configuration
1. Clone repo to desired location
2. Install scripts to iTerm2's AutoLaunch folder with via `bash ./install.sh`
3. Close and relaunch iTerm
4. Follow [the instructions for using status bar components](https://www.iterm2.com/3.3/documentation-status-bar.html) and drag them where you like

**Note** You may be prompted to download, configure and activate the Python runtime for iTerm


## Components Overview

### Bitcoin Price
![btc_price](screenshots/btc_price.png)

Displays the current Bitcoin price in USD. Updates every 15 seconds.

### Bitcoin Halvening Countdown
![btc_halvening](screenshots/btc_halvening.png)

Displays the halvening completion percentage and the number of unmined blocks to be found before the halvening.  Updated every 5 minutes.

### Bitcoin Mempool
![mempool_size](screenshots/btc_mempool.png)

Display mempool unconfirmed transaction count and size in MB. Updates every minute.


## TODOs
- [ ] Component: ETH Price
- [ ] Component: LTC Price
- [ ] Upgrade: BTC Price: Choose fiat currency
- [ ] Upgrade: BTC Price: Show 24hr increase or decrease icon
