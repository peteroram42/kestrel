# kestrel

Kestrel is a python backend service that is still a work in progress (as a side project). 

When completed, it connects to CoinMarketCap and pulls cryptocurrency prices, as well as Yahoo finance to pull stock quotes. 

A user registers which coins and stocks he wants to watch and what price point (fixed price point, or +/- an amount or %) he wants to get notified about. 

Kestrel pulls prices and quotes once a minute (cadence can be adjusted), and sends alerts (email or sms) when price change triggers a notification. 

This way you don't miss buy or sell points, or when there's a lot of action you don't want to miss, without having to be preoccupied or fixated.
