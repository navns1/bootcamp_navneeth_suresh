# Stakeholder Memo: Does the 52-Week High Effect Still Hold?

To: Portfolio Manager
From: Junior Analyst
Re: Replication test of the 52-week high anomaly

## The Pain Point

The 52-week high effect is a documented pattern where stocks trading near their highs tend to keep outperforming, first shown by George and Hwang (2004). Documented in academic research doesn't mean it still holds today. Before the desk spends time researching it further, someone needs to check whether it shows up in recent data for a realistic basket of liquid stocks.

## What This Analysis Does

Using about 2 to 3 years of daily prices for 15 to 20 liquid, large cap stocks, this project runs two tests. A regression checks whether distance from the 52-week high predicts the size of forward returns. A classifier checks whether it predicts direction, up or down, better than a naive baseline. Both tests are run across more than one forward return window, such as 5 day and 20 day, to check the result isn't just an artifact of one arbitrary choice.

## Why This Is Useful and What It Isn't

This is descriptive and predictive, not causal. It replicates a pattern rather than explaining the mechanism behind it, and it isn't back tested as a strategy or checked against transaction costs. What it gives the desk is a quick, honest read on whether the effect is worth further research time.

## Assumptions the Desk Should Know

The sample is 15 to 20 currently listed, liquid names over 2 to 3 years, which is much smaller and more recent than the original academic studies. Only stocks still trading today are included, which can inflate the apparent effect through survivorship bias. There are no sector or market wide controls, so part of any effect found could reflect broader momentum rather than the 52-week high signal specifically. A 2021 follow up study by Barroso and Wang also found the original effect mostly shows up in small cap stocks and may overlap heavily with plain price momentum, so results here will be checked against a simple momentum benchmark.

## Key Risk

If the effect doesn't hold in this sample, that is still a useful finding. It would tell the desk not to prioritize this angle without a larger, more careful study, and since this sample is much smaller than the original research, a null result here wouldn't actually contradict the published literature. Results will be reported honestly either way, including across multiple forward return windows to show whether the finding is robust or fragile.

## Ask

Nothing needed from the desk right now. This is a scoping memo. Notebook and slide deck to follow once modeling is complete.
