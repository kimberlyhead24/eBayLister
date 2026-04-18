## Live market data and pricing intelligence
- [ ] Add live market data source to system design for current pricing support.
- [ ] Research eBay Browse API for active listing search and item summary retrieval. [web:418][web:419]
- [ ] Define search query generation from classified item name, brand, category, and condition.
- [ ] Build market-data module that pulls current active listing prices from eBay API.
- [ ] Decide how sold-price evidence will be collected: official data source, approved third-party API, or manual import. [web:423]
- [ ] Normalize current listing prices, shipping, and condition into a comparable pricing table.
- [ ] Add confidence score for market-data quality when search results are weak or noisy.
- [ ] Add fallback rule when no reliable market comps are found.

## Item classification and search
- [ ] Expand item-classification model requirements to support market search query generation.
- [ ] Output structured fields from image classification: probable item name, brand, category, model, condition clues.
- [ ] Build query constructor that turns classification output into eBay market searches.
- [ ] Test whether classification output is good enough to retrieve correct market comps.
- [ ] Add manual correction flow when classification is inaccurate.

## Pricing engine updates
- [ ] Update pricing engine to combine live market data, sold comps, seller rules, and profit floor.
- [ ] Separate price recommendation into quick sale, competitive listing, and premium listing.
- [ ] Add rule to ignore obvious outlier listings when computing market value.
- [ ] Add fee and shipping adjustments before final price recommendation.
- [ ] Add explanation output showing why each price was suggested.

## RAG and knowledge base updates
- [ ] Clarify in project docs that RAG is used for rules and guidance, not as the only pricing source.
- [ ] Store seller workflow notes, listing rules, shipping preferences, and disclaimer templates in the knowledge base.
- [ ] Keep market-price retrieval separate from RAG retrieval.